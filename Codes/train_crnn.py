import sys
import os
import tensorflow as tf

sys.path.append("..\\libs")
from classification import input_data
from classification import models
from classification import trainer
from classification import freeze
from tensorflow.python.client import device_lib

# Setting up GPU
print(device_lib.list_local_devices())
tf.test.gpu_device_name()
tf.device('/gpu:0')


### Flag Initialization ###
flags=tf.app.flags
flags=tf.app.flags

# Intializing Source Directories
flags.DEFINE_string('data_dir','F:\\ML_Project\\Data\\','Train Data Folder')
flags.DEFINE_string('summaries_dir','F:\\ML_Project\\Data\\summaries\\','Summaries Folder')
flags.DEFINE_string('train_dir','F:\\ML_Project\\Data\\logs&checkpoint\\','Directory to write event logs and checkpoint')
flags.DEFINE_string('models_dir','F:\\ML_Project\\models\\','Models Folder')

# Intializing Task Specific Parameters
flags.DEFINE_string('wanted_words','yes,no,up,down,left,right,on,off,stop,go','Wanted Words')
flags.DEFINE_float('validation_percentage',10,'Validation Percentage')
flags.DEFINE_float('testing_percentage',10,'Testing Percentage')
flags.DEFINE_integer('sample_rate',16000,'Sample Rate')
flags.DEFINE_integer('clip_duration_ms',1000,'Clip Duration in ms')
flags.DEFINE_float('window_size_ms',40,'How long each spectogram timeslice is')
flags.DEFINE_float('window_stride_ms',20.0,'How far to move in time between frequency windows.')
flags.DEFINE_integer('dct_coefficient_count',40,'How many bins to use for the MFCC fingerprint')
flags.DEFINE_float('time_shift_ms',100.0,'Range to randomly shift the training audio by in time.')

FLAGS=flags.FLAGS

# Initializing Variables
model_architecture='c_rnn'
start_checkpoint=None
logging_interval=10
eval_step_interval=500
save_step_interval=2000
silence_percentage=10.0
unknown_percentage=10.0
background_frequency=0.8
background_volume=0.3
learning_rate='0.0005,0.0001,0.00002' # Training with different learning rates for different iterations
train_steps='10000,10000,10000'       # No. of iterations for each learning rate  
batch_size=256
model_size_info=[48, 10, 4, 2, 2, 2, 60, 84]

#Initialise the get_train_data() get_val_data() and get_test_data() Function

train_dir=os.path.join(FLAGS.data_dir,'train','audio')
model_settings = models.prepare_model_settings(
      len(input_data.prepare_words_list(FLAGS.wanted_words.split(','))),
      FLAGS.sample_rate, FLAGS.clip_duration_ms, FLAGS.window_size_ms,
      FLAGS.window_stride_ms, FLAGS.dct_coefficient_count)
audio_processor = input_data.AudioProcessor(
      train_dir, silence_percentage, unknown_percentage,
      FLAGS.wanted_words.split(','), FLAGS.validation_percentage,
      FLAGS.testing_percentage, model_settings,use_silence_folder=True)
def get_train_data(args):
    sess=args
    time_shift_samples = int((FLAGS.time_shift_ms * FLAGS.sample_rate) / 1000)
    train_fingerprints, train_ground_truth = audio_processor.get_data(
        batch_size, 0, model_settings,background_frequency,
        background_volume, time_shift_samples, 'training', sess)
    return train_fingerprints,train_ground_truth
def get_val_data(args):
    '''
    Input: (sess,offset)
    '''
    sess,i=args
    validation_fingerprints, validation_ground_truth = (
            audio_processor.get_data(batch_size, i, model_settings, 0.0,
                                     0.0, 0, 'validation', sess))
    return validation_fingerprints,validation_ground_truth
def get_test_data(args):
    '''
    Input: (sess,offset)
    '''
    sess,i=args
    test_fingerprints, test_ground_truth = audio_processor.get_data(
        batch_size, i, model_settings, 0.0, 0.0, 0, 'testing', sess)
    return test_fingerprints,test_ground_truth
def main(_):
    sess=tf.InteractiveSession()
    # Placeholders
    fingerprint_size = model_settings['fingerprint_size']
    label_count = model_settings['label_count']
    fingerprint_input = tf.placeholder(
      tf.float32, [None, fingerprint_size], name='fingerprint_input')
    ground_truth_input = tf.placeholder(
      tf.float32, [None, label_count], name='groundtruth_input')
    set_size = audio_processor.set_size('validation')
    label_count = model_settings['label_count']
    
    # Create Model
    
    logits, dropout_prob = models.create_model(
      fingerprint_input,
      model_settings,
      model_architecture,
      model_size_info=model_size_info,
      is_training=True)
    
    #Start Training
    extra_args=(dropout_prob,label_count,batch_size,set_size)
    trainer.train(sess,logits,fingerprint_input,ground_truth_input,get_train_data,
                  get_val_data,train_steps,learning_rate,eval_step_interval, logging_interval=logging_interval,
                  start_checkpoint=start_checkpoint,checkpoint_interval=save_step_interval,
                  model_name=model_architecture,train_dir=FLAGS.train_dir,
                  summaries_dir=FLAGS.summaries_dir,args=extra_args)
tf.app.run(main=main)
save_checkpoint='F:\\ML_Project\\Data\\logs&checkpoint\\c_rnn\\ckpt-30000'
save_path=os.path.join(FLAGS.models_dir,model_architecture,'%s-batched.pb'%os.path.basename(save_checkpoint))
freeze.freeze_graph(FLAGS,model_architecture,save_checkpoint,save_path,batched=True,model_size_info=model_size_info)
save_path=os.path.join(FLAGS.models_dir,model_architecture,'%s-batched.pb'%os.path.basename(save_checkpoint))
freeze.freeze_graph(FLAGS,model_architecture,save_checkpoint,save_path,batched=True,model_size_info=model_size_info)

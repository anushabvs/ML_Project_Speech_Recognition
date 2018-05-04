import tensorflow as tf
import os
import sys
import numpy as np
import pandas as pd


sys.path.append("../libs")
from classification import label_wav
from classification import input_data
from classification import models
from tensorflow.python.platform import gfile

flags=tf.app.flags
#Important Directories
flags.DEFINE_string('data_dir','C:\\Users\\klp\\Downloads\\ML_Mahera\\Data\\','Train Data Folder')
flags.DEFINE_string('summaries_dir','C:\\Users\\klp\\Downloads\\ML_Mahera\\Data\\summaries','Summaries Folder')
flags.DEFINE_string('results_dir','C:\\Users\\klp\\Downloads\\ML_Mahera\\Data\\results','Directory to write event logs and checkpoint')
flags.DEFINE_string('models_dir','C:\\Users\\klp\\Downloads\\ML_Mahera\\models\\','Models Folder')
flags.DEFINE_string('predictions_dir','C:\\Users\\klp\\Downloads\\ML_Mahera\\predictions','Predictions Directory')
flags.DEFINE_string('wanted_words','yes,no,up,down,left,right,on,off,stop,go','Wanted Words')
FLAGS=flags.FLAGS

#Variables
model_architecture='c_rnn'
model_version='30000'
test_dir=os.path.join(FLAGS.data_dir,'test','*.wav')
testing_files_list=sorted(gfile.Glob(test_dir))

#Predict
labels_list=input_data.prepare_words_list(FLAGS.wanted_words.split(','))
graph=os.path.join(FLAGS.models_dir,model_architecture,'ckpt-'+model_version+'-small-batched.pb')
pred_mat,pred=label_wav.label_wav_batched(testing_files_list,labels_list,graph,batch_size=1000)
print(pred_mat)
print(pred)
save_folder='r_cnn_output'
save_path=os.path.join(FLAGS.predictions_dir,save_folder)
if not os.path.exists(save_path):
    os.makedirs(save_path)
f_names=[]
for f in testing_files_list:
    f_names.append(os.path.basename(f))
pred_df=pd.DataFrame({'fname':f_names,'label':pred})
pred_df.to_csv(os.path.join(save_path,'predictions.csv'),index=None)
print(pred_df)

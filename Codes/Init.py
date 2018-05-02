import sys
sys.path.append("..\\libs")
from classification import utils
data_dir='F:\\ML_Project\\Data\\'
sample_dir='F:\ML_Project\Data\\sample\\'
#initialize the Dataset
dataset=utils.Dataset(data_dir)
# Split into Train, Val and Test Sets
dataset.split_train_test_val()
# Generate the Sample Dataset
dataset.gen_sample_set(sample_dir=sample_dir)
# Print Dataset Statistics
dataset.print_dataset_stats()

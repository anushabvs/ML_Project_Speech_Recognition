import sys
sys.path.append("..\\libs")
from classification import utils

data_dir='F:\\ML_Project\\Data\\'
sample_dir='F:\ML_Project\Data\\sample\\'

# Initializing the Dataset
dataset=utils.Dataset(data_dir)

# Splitting into Training and Testing datasets
dataset.split_train_test_val()

# Print Dataset Statistics
dataset.print_dataset_stats()

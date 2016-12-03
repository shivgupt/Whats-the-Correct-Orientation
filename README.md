# a6 - image orientation detector

# Useage:
 - `python orient.py train_file test_file mode extra`

where
 - train_file is the training data file name
 - test_file is the test data file name
 - mode is one of 'nearest', 'adaboost', 'nnet', or 'best'

# 'extra' argument:
 - should be omitted if mode == 'nearest'
 - is the number of decision stumps if mode == 'adaboost'
 - is the number of hidden layer nodes if mode == 'nnet'
 - is the model filename if mode == 'best'

# A full test of all the code in this program can be achieved with the following:

 - `python orient.py train-data.txt test-data.txt nearest`          # 0 - 0 seconds
 - `python orient.py train-data.txt test-data.txt adaboost 5`       # 0 - 0 seconds
 - `python orient.py train-data.txt test-data.txt nnet 5`           # 0 - 0 seconds
 - `python orient.py train-data.txt test-data.txt best model_file`  # 0 - 0 seconds

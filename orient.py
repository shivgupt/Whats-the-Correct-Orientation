#!/usr/bin/python

"""
____________________________________________________________

1. Formulation/Abstractions
____________________________________________________________


____________________________________________________________

2. How my program works
____________________________________________________________

Useage:
 $ ./spam mode technique dataset-directory model-file

where - mode is one of 'test' or 'train'
      - technique is one of 'dt' or 'bayes'
      - dataset-directory is the name of a directory containing test/ and train/
      - model-file is the filename to either write to if mode == 'train'
        or read from if mode == 'test'

Assuming the test/ and train/ data is in a folder called 'data',
a full test of all the code in this module can be achieved with the following:

 $ ./spam train bayes data model   # 7  - 10 seconds runtime
 $ ./spam test bayes data model    # 4  - 7  seconds runtime
 $ ./spam train dt data model      # 22 - 25 seconds runtime
 $ ./spam test dt data model       # 1  - 4  seconds runtime

The first commands will write out a file called model.
The second will read the model file and print bayes classification results
The third will overwrite the old model file and replace it with one for dt
The fourth will read the new model file and print dt classification results

____________________________________________________________

3. Problems/Assumptions/Simplifications
____________________________________________________________



____________________________________________________________

4.
____________________________________________________________


"""

import sys
import os
import pickle

# k-nearest-neighbors
if len(sys.argv) == 4 and sys.argv[3] == 'nearest': # nearest


    print "KNN activated!"


# adaboost
elif len(sys.argv) == 5 and sys.argv[3] == 'adaboost':
    try:
        stumps = int(sys.argv[4])
    except ValueError:
        print " Invalid number of stumps:", sys.argv[4]
        sys.exit()


    print "Adaboost activated!"


# neural network
elif len(sys.argv) == 5 and sys.argv[3] == 'nnet':
    try:
        nnodes = int(sys.argv[4])
    except ValueError:
        print " Invalid number of stumps:", sys.argv[4]
        sys.exit()


    print "Neural Network activated!"


elif len(sys.argv) == 5 and sys.argv[3] == 'best':
    try:
        model = pickle.load(open(sys.argv[4], 'rb'))
    except EnvironmentError:
        print " Invalid model file:", sys.argv[4]
        sys.exit()


    print "Best activated!"


else:
    print "\n Invalid:", sys.argv
    print "\n Useage: python orient.py train_file test_file mode flavor?\n"

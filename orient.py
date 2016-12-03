#!/usr/bin/python

"""
____________________________________________________________

1. Formulation/Abstractions
____________________________________________________________


____________________________________________________________

2. How my program works
____________________________________________________________

see README.md

____________________________________________________________

3. Problems/Assumptions/Simplifications
____________________________________________________________



____________________________________________________________

4.
____________________________________________________________


"""

import sys
import pickle

import nearest
import adaboost
import nnet


# Load training data
try:
    with open(sys.argv[1]) as trainf:
        traind = [x.rstrip().split(' ') for x in trainf.readlines()]
except IOError:
    print " Invalid training data filename:", sys.argv[1]
    sys.exit()


# load testing data
try:
    with open(sys.argv[2]) as testf:
        testd = [x.rstrip().split(' ') for x in testf.readlines()]
except IOError:
    print " Invalid testing data filename:", sys.argv[2]
    sys.exit()


# activate k-nearest-neighbors
if len(sys.argv) == 4 and sys.argv[3] == 'nearest': # nearest

    nearest.train(traind)
    nearest.test(testd)


# activate adaboost
elif len(sys.argv) == 5 and sys.argv[3] == 'adaboost':
    try:
        stumps = int(sys.argv[4])
    except ValueError:
        print " Invalid number of stumps:", sys.argv[4]
        sys.exit()

    adaboost.train(traind, stumps)
    adaboost.test(testd, stumps)


# activate neural network
elif len(sys.argv) == 5 and sys.argv[3] == 'nnet':
    try:
        nnodes = int(sys.argv[4])
    except ValueError:
        print " Invalid number of hidden nodes:", sys.argv[4]
        sys.exit()

    nnet.train(traind, nnodes)
    nnet.test(testd, nnodes)


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

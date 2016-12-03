#!/usr/bin/python
"""
Adaboost
"""


import time


def train(traind, N):
    starttime = time.time()
    print " Training...",
    print "Done in", round(time.time() - starttime, 5), "seconds!"


def test(testd, N):
    starttime = time.time()
    print " Testing...",
    print "Done in", round(time.time() - starttime, 5), "seconds!"

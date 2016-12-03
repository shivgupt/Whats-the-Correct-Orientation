#!/usr/bin/python
"""
K-Nearest Neighbor Implementation
"""


import time


def train(traind):
    starttime = time.time()
    print " Training...",
    print "Done in", round(time.time() - starttime, 5), "seconds!"


def test(testd):
    starttime = time.time()
    print " Testing...",
    print "Done in", round(time.time() - starttime, 5), "seconds!"

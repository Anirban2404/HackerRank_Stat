#!/bin/python

import sys
'''
Given an array, X, of N integers and an array, W, representing the respective weights of X's 
elements, calculate and print the weighted mean of X's elements. Your answer should be rounded 
to a scale of 1 decimal place (i.e., 12.3 format).
'''

# WEIGHTED MEAN #
def fn_wmean(myList,myweightedList):
    sum = 0
    wsum = 0
    for i in range(len(myList)):
        sum =  float(sum + (myList[i] * myweightedList[i]))
        wsum = float(wsum + myweightedList[i])
    return float(sum / wsum);

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    i = 0;
    numlist = map(int, raw_input().strip().split(' '))
    weightedList = map(int, raw_input().strip().split(' '))
    weightedMean = fn_wmean(numlist,weightedList)
    print "Weighted Mean: %.1f " % weightedMean

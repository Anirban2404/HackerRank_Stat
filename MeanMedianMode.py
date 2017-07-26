#!/bin/python

import sys
'''
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
If your array contains more than one modal value, choose the numerically smallest one.'''

# MEAN #
def fn_mean(myList):
    return sum(myList)/len(myList)

# MEDIAN #
def fn_median(myList):
    myList.sort()
    mid = (len(myList)+1)/2
    if (len(myList)%2 == 0):
        return (myList[mid-1] + myList[mid])/2
    else:
        return myList[mid - 1]

# MODE #
def fn_mode(myList):
    return max(myList, key=myList.count)
    #return modelist[0]

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    i = 0;
    numlist = []
    numlist = map(float, raw_input().strip().split(' '))
    mean = fn_mean(numlist)
    median = fn_median(numlist)
    mode = fn_mode(numlist)
    print "Mean: ",mean
    print "Median: ", median
    print "Mode: ", int(mode)
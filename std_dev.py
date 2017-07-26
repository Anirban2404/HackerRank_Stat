#!/bin/python

import sys
'''
Given an array, X, of N integers, calculate and print the standard deviation. Your answer should be in decimal form, 
rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +/- 0.1 will be tolerated 
for the standard deviation.
'''

# MEAN #
def fn_mean(myList):
    return sum(myList)/len(myList)

# MEAN #
def fn_std_dev(myList,mean):
    sum = 0
    for i in range(len(myList)):
        sum = sum + (myList[i] - mean)**2;
    variance = sum / len(myList)
    std_dev = variance ** 0.5
    return std_dev

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    i = 0;
    numlist = []
    numlist = map(float, raw_input().strip().split(' '))
    mean = fn_mean(numlist)
    std_dev = fn_std_dev(numlist,mean)
    print "Mean: ", mean
    print "Standard Deviation: %.1f" % std_dev


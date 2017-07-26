#!/bin/python

import sys

'''
Given an array, X , of n integers, calculate the respective first quartile (Q1), second quartile (Q2), 
and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.

The quartiles of an ordered data set are the  points that split the data set into  equal groups. The  quartiles are defined as follows:

1. Q1: The first quartile is the middle number between the smallest number in a data set and its median.
2. Q2: The second quartile is the median (50th percentile) of the data set.
3. Q3: The third quartile is the middle number between a data set's median and its largest number.

'''

# MEDIAN #
def fn_median(myList):
    myList.sort()
    mid = (len(myList)+1)/2
    if (len(myList)%2 == 0):
        return (myList[mid-1] + myList[mid])/2
    else:
        return myList[mid - 1]

#def fn_quartile():

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    i = 0;
    numlist = map(int, raw_input().strip().split(' '))
    q2 = fn_median(numlist)
    mid = (len(numlist) + 1) / 2
    if (len(numlist) % 2 !=0):
        qlist1 = numlist[:mid-1]
        qlist2 = numlist[mid:]
    else:
        qlist1 = numlist[:mid]
        qlist2 = numlist[mid:]
    q1 = fn_median(qlist1)
    q3 = fn_median(qlist2)
    print "Q1: ", q1
    print "Q2: ", q2
    print "Q3: ", q3
#!/bin/python

import sys

'''
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3 - Q1 ).

Given an array, X, of n integers and an array, F, representing the respective frequencies of X's elements, 
construct a data set, S, where each xi occurs at frequency fi. Then calculate and print S's interquartile range, 
rounded to a scale of 1 decimal place (i.e., 123 format).

1. Q1: The first quartile is the middle number between the smallest number in a data set and its median.
2. Q2: The second quartile is the median (50th percentile) of the data set.
3. Q3: The third quartile is the middle number between a data set's median and its largest number.

'''

# MEDIAN #
def fn_median(myList):
    myList.sort()
    mid = (len(myList)+1)/2
    if (len(myList)%2 == 0):
        return float((myList[mid-1] + myList[mid])/2)
    else:
        return float(myList[mid - 1])

#def fn_quartile():

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    i = 0;
    numList = map(int, raw_input().strip().split(' '))
    freqList = map(int, raw_input().strip().split(' '))
    inputList=[]
    for i in range(x):
        for j in range(freqList[i]):
            #print freqList[i]
            inputList.append(numList[i])
    #print inputList
    q2 = fn_median(inputList)
    mid = (len(inputList) + 1) / 2
    if (len(inputList) % 2 !=0):
        qlist1 = inputList[:mid-1]
        qlist2 = inputList[mid:]
    else:
        qlist1 = inputList[:mid]
        qlist2 = inputList[mid:]
    q1 = fn_median(qlist1)
    q3 = fn_median(qlist2)
    #print "Q1: ", q1
    #print "Q2: ", q2
    #print "Q3: ", q3
    print "Interquartile Range : ", q3 - q1
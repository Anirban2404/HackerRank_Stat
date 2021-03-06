#!/bin/python

import sys
'''
Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. 
If your array contains more than one modal value, choose the numerically smallest one.'''

# MEAN #
def fn_mean(myList):
    return sum(myList)/len(myList)

# STANDARD DEVIATION #
def fn_std_dev(myList,mean):
    sum = 0
    for i in range(len(myList)):
        sum = sum + (myList[i] - mean)**2;
    variance = sum / len(myList)
    std_dev = variance ** 0.5
    return std_dev

# RANK #
def fn_rank(myList):
    sortedList = sorted(myList)
    #print sortedList
    ranklist = []
    for i in range(len(myList)):
        for j in range(len(sortedList)):
            if myList[i] == sortedList[j]:
                #print myList[i], j+1
                ranklist.append(j+1)
    return ranklist

# MAIN #
if __name__ == "__main__":
    x = int(raw_input().strip())
    xlist = map(float, raw_input().strip().split(' '))
    xmean = fn_mean(xlist)
    ylist = map(float, raw_input().strip().split(' '))
    ymean = fn_mean(ylist)
    #print "XMean: ", xmean
    #print "YMean: ", ymean
    x_std_dev = fn_std_dev(xlist, xmean)
    y_std_dev = fn_std_dev(ylist, ymean)
    #print "X_std_dev: %.3f" % x_std_dev
    #print "Y_std_dev: %.3f" % y_std_dev
    sum = 0.0
    x_rankList = fn_rank(xlist)
    #print x_rankList
    y_rankList = fn_rank(ylist)
    #print y_rankList

    '''
    for i in range (x):
        sum = sum + (xlist[i] - xmean) * (ylist[i] - ymean)
    
    
    denominator = x * x_std_dev * y_std_dev
    Pearson_correlation_coefficient = sum / denominator
    #print "%.3f" % Pearson_correlation_coefficient
    '''
    for i in range(x):
        sum = sum + ((x_rankList[i] - y_rankList[i]) ** 2)
    denominator = x * ( x**2 - 1)
    #print sum
    #print denominator
    spearman_correlation_coefficient = 1 - 6 * sum / denominator
    print "%.3f" %  spearman_correlation_coefficient
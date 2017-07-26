#!/bin/python

import sys

'''
The probability that a machine produces a defective product is 1/3 . What is the probability that the 
1st defect is found during the 5th inspection?
'''

# MAIN #
if __name__ == "__main__":
    inputList = map(float, raw_input().strip().split(' '))
    # sum = inputList[0] + inputList[1]
    prob_numerator = inputList[0]
    prob_denominator = inputList[1]
    probability = prob_numerator / prob_denominator
    num_times = map(int, raw_input().strip().split(' '))
    n = num_times[0]
    prob_defect = 0
    for i in range (1, n+1):
        prob_defect = prob_defect + ((1 - probability) ** (i - 1)) * probability
    print "%.3f" % prob_defect
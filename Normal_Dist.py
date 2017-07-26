#!/bin/python

import sys

'''
In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution 
with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be 
assembled at this plant in:

1. Less than 19.5 hours?
2. Between 20 and 22 hours?

The final grades for a Physics exam taken by a large group of students have a mean of 70
and a standard deviation of 10. If we can approximate the distribution of these grades 
by a normal distribution, what percentage of the students:

1. Scored higher than 80 (i.e., have a grade > 80 )?
2. Passed the test >=60(i.e., have a grade >= 60 )?
3. Failed the test <60 (i.e., have a grade < 60 )?
Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

'''


# MAIN #
if __name__ == "__main__":
    inputList = map(float, raw_input().strip().split(' '))
    mean = inputList[0]
    std_dev = inputList[1]
    cond1essThan = float(raw_input().strip())
    #condBetween = map(float, raw_input().strip().split(' '))
    condgrtrThan = float(raw_input().strip())
    #P(x < 19.5)
    #z_score_195 = (cond1essThan - mean) / std_dev
    z_score_60 = (cond1essThan - mean) / std_dev
    #print z_score_195
    #print z_score_60
    z_025 = .4013
    z_1 = .8413
    #print z_1
    #print z_025
    #P(20 < X < 22)
    '''
    z_score_20 = (condBetween[0] - mean) / std_dev
    z_score_22 = (condBetween[1] - mean) / std_dev
    #print z_score_20
    #print z_score_22
    z_0 = .5
    z_1 = .8413
    print z_1 - z_0
    '''
    z_score_80 = (condgrtrThan - mean) / std_dev
    z_m1 = 0.1587
    print z_m1 * 100
    print z_1 * 100
    print (1 - z_1)*100
#!/bin/python

import sys

'''
A random variable, X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.
'''

def factorial(x):
    fact = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            fact = fact * i
        return fact

# MAIN #
if __name__ == "__main__":
    mean = float(raw_input().strip())
    k = int(raw_input().strip())
    e = 2.71828
    probability = ((mean ** k )/ factorial(k)) * e ** (-mean)
    print "%.3f" % probability
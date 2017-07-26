#!/bin/python

import sys

'''
The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day's operation:
- The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. 
  The daily cost of operating A is CA = 160 + 40X2.
- The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. 
  The daily cost of operating B is CB = 128 + 40Y2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly 
to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.
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
    inputList = map(float, raw_input().strip().split(' '))
    XA = inputList[0]
    XB = inputList[1]
    costA = 160 + 40 * (XA + ( XA ** 2))
    print "%.3f" % costA
    costB = 128 + 40 * (XB + (XB ** 2))
    print "%.3f" % costB
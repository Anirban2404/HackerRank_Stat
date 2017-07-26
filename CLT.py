#!/bin/python

import sys

'''
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes 
must be transported via the elevator. The box weight of this type of cargo follows a distribution 
with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, 
what is the probability that 49 all boxes can be safely loaded into the freight elevator and transported?

'''

'''
The number of tickets purchased by each student for the University X vs. University Y football game follows
 a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are 
only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?
'''

'''
You have a sample of 100 values from a population with mean 500 and with standard deviation 80. 
Compute the interval that covers the middle 95% of the distribution of the sample mean; 
in other words, compute A and B such that P(A < X < B ) = 0.95. Use the value of z = 1.96. 
Note that z is the z-score.
'''
# MAIN #
if __name__ == "__main__":
    #max = int(raw_input().strip())
    num_of_elements = int(raw_input().strip())
    #mean = int(raw_input().strip())
    #std_dev = int(raw_input().strip())
    mean = float(raw_input().strip())
    std_dev = float(raw_input().strip())
    prob = float(raw_input().strip())
    Z_score = float(raw_input().strip())
    # P ( Xk << 98800 ) = P ( X - n * mean / n^.5 * std_dev)
    # z_score = (max - num_of_elements * mean) / ((num_of_elements ** 0.5) * std_dev)
    # print z_score
    # z_05 = 0.6915
    #z_233 = 0.0099
    #print z_233
    # print z_05

    # Z_score = (A - mean) / (std_dev/ (num_of_elements ** 0.5))
    A = - Z_score * (std_dev / (num_of_elements ** 0.5)) + mean
    print A

    B = Z_score * (std_dev/ (num_of_elements ** 0.5)) + mean
    print B
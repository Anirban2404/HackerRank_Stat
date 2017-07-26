#!/bin/python

import sys

'''
The ratio of boys to girls for babies born in Russia is 1.09:1. 
If there is  child born per birth, what proportion of Russian families 
with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, 
rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''


def factorial(x):
    fact = 1
    if x == 0:
        return 1
    else:
        for i in range(1, x + 1):
            fact = fact * i
        return fact


def fn_least(prob_boy, prob_girl, num_children, at_lst_cond):
    i = at_lst_cond
    sum = 0
    for i in range(at_lst_cond, num_children + 1):
        choose = factorial(num_children) / (factorial(i) * factorial(num_children - i))
        #print choose
        sum = sum + choose * (prob_boy ** i) * prob_girl ** (num_children - i)
        #print sum
    return sum


def fn_most(prob_boy, prob_girl, num_children, at_mst_cond):
    i = at_mst_cond
    sum = 0
    for i in range(0, at_mst_cond + 1):
        choose = factorial(num_children) / (factorial(i) * factorial(num_children - i))
        #print choose
        sum = sum + choose * (prob_boy ** i) * prob_girl ** (num_children - i)
        #print sum
    return sum


# MAIN #
if __name__ == "__main__":
    inputList = map(float, raw_input().strip().split(' '))
    # sum = inputList[0] + inputList[1]
    prob_boy = float(inputList[0] / 100)
    prob_girl = float(1 - prob_boy)
    num_children = int(inputList[1])
    at_lst_cond = 2
    at_mst_cond = 2

    prob_lst = fn_least(prob_boy, prob_girl, num_children, at_lst_cond)
    prob_mst = fn_most(prob_boy, prob_girl, num_children, at_mst_cond)
    print "Prob Least: %.3f" % prob_lst
    print "Prob Most: %.3f" % prob_mst

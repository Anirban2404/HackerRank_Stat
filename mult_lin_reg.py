#!/bin/python

import sys
from sklearn import linear_model

'''
Andrea has a simple equation:
Y = a + b1.f1 + b1.f2 + . . . + bm.fm
for (m + 1) real constants (a, f1, f2, ... , fm ). We can say that the value of Y depends on
m features. Andrea studies this equation for n different feature sets (f1, f2, ... , fm ) and 
records each respective value of Y. If she has q new feature sets, can you help Andrea find 
the value of Y for each of the sets?
'''


# MAIN #
if __name__ == "__main__":
    input = map(int, raw_input().strip().split(' '))
    m = input[0]
    num = input[1]
    xlist = []
    ylist = []

    for i in range(num):
        list1 = map(float, raw_input().strip().split(' '))
        list = []
        for j in range(m):
            list.append(list1[j])
        xlist.append(list)
        ylist.append(list1[m])

    #print xlist
    #print ylist
    lm = linear_model.LinearRegression()
    lm.fit(xlist, ylist)
    a = lm.intercept_
    b = lm.coef_
    rep = int(raw_input().strip())
    y_value = []

    for j in range(rep):
        msum = 0.0
        inp = map(float, raw_input().strip().split(' '))
        for k in range(m):
            msum = msum + (b[k] * inp[k])
            #print b[j]
            #print inp[k]
            y_val = msum + a
        y_value.append(y_val)
    for j in range(rep):
        print "%.2f" % y_value[j]
#!/bin/python

import sys

'''
A group of five students enrolls in Statistics immediately after taking a Math aptitude test. 
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed 
as the following list of (x,y) points:

1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve 
in Statistics? Determine the equation of the best-fit line using the least squares method, then 
compute and print the value of when x = 80.
'''


# MEAN #
def fn_mean(myList):
    return sum(myList) / len(myList)

def coef_(myList1,myList2):
    xmean = fn_mean(myList1)
    ymean = fn_mean(myList2)
    #print xmean
    #print ymean
    sumx = 0.0
    for i in range(len(myList1)):
        sumx = sumx + myList1[i]**2
    #print sumx
    sumxy = 0.0
    for i in range(len(myList1)):
        sumxy = sumxy + myList1[i] * myList2[i]
    #print sumxy
    sum_x1 = sum(myList1)
    sum_y1 = sum(myList2)
    coeff = ((len(myList1)* sumxy) - (sum_x1 * sum_y1))/((len(myList1) * sumx) - sum_x1**2)
    #print coeff
    intercept_ = ymean - coeff*xmean
    #print intercept_
    lin_reg = []
    lin_reg.append(intercept_)
    lin_reg.append(coeff)
    return lin_reg

# MAIN #
if __name__ == "__main__":
    list1 = map(int, raw_input().strip().split(' '))
    list2 = map(int, raw_input().strip().split(' '))
    list3 = map(int, raw_input().strip().split(' '))
    list4 = map(int, raw_input().strip().split(' '))
    list5 = map(int, raw_input().strip().split(' '))
    xlist = []
    xlist.append(list1[0])
    xlist.append(list2[0])
    xlist.append(list3[0])
    xlist.append(list4[0])
    xlist.append(list5[0])

    ylist = []
    ylist.append(list1[1])
    ylist.append(list2[1])
    ylist.append(list3[1])
    ylist.append(list4[1])
    ylist.append(list5[1])

    #print xlist
    #print ylist
    lin_reg = coef_(xlist, ylist)
    intercept_ = lin_reg[0]
    #print intercept_
    coef_ = lin_reg[1]
    #print coef_
    y_value = intercept_ + coef_ * 80
    print y_value

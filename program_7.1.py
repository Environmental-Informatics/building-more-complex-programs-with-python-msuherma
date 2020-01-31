#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:11:12 2020

@author: msuherma
Exercise from
Downey, A., (2015). Think Python, 2nd Edition. Safari, an O'Reilly Media Company.
"""

#Exercise 7.1
import math

def mysqrt(a):                      # my sqrt function
    epsilon = 0.0000001             # determined epsilon number to get closer enough
    x = 5.00000
    while True:                     # To break the loop
        y = (x + a/x) / 2
        if abs(y - x) < epsilon:    # using absolute value is safer than exact x = y
            return y
            break
        x = y
        
    
def test_square_root():
    '''This is to print the test_square_root as sample table in Exercise 7.1
    '''    
    print ("a    mysqrt(a)       math.sqrt(a)      diff")   # to create headline
    print ("-    ---------       ------------      ----")   # to create separator dashes with the results
    for a in range(1,11):                                   # to print a 1-9 showing in the table
        print ("%.1f  %.11f   %.12f    %.20f" %(a, mysqrt(a), math.sqrt(a), mysqrt(a) - math.sqrt(a)))
        # this % input here is to make sure the printed result is align with the header (%.nf = n is number of decimal shown)

#print(math.sqrt(4))
#print(mysqrt(4))
test_square_root()

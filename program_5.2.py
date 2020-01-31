#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:25:06 2020

@author: msuherma
"""

# Exercise 5.2 Check Fermat

#import math

def check_fermat(a, b, c, n):                       # check_fermat function, taking a,b,c,n as parameters
    if n > 2 and a**n + b**n == c**n:               # from the equation assigned in the 5.2
        print ("Holy Smoke! Fermat was wrong!")     # print this if 
    else:
        print ("No, that does not work.")
        

def cf_input():                                     # to print input inquiry in the console
    a = int(input("write 'a' value here: "))        # int(input...) is to convert the input to be integer instead of string
    b = int(input("write 'b' value here: "))
    c = int(input("write 'c' value here: "))
    n = int(input("write 'n' value here: "))
    return check_fermat(a, b, c, n)

cf_input()
    
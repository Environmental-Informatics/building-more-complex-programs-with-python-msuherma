#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 11:00:23 2020

@author: msuherma
Exercise from
Downey, A., (2015). Think Python, 2nd Edition. Safari, an O'Reilly Media Company.
"""

# Excercise 6.5

def gcd(a, b):
    a = int(a)      # this to convert any input of a to integer
    b = int(b)      # convert b to integer
    if a > b:       # using if, elif, else conditionals; if a is greater than b
        c = a - b   # then c is a - b
        gcd(b,c)    # gcd is then taking b and c as parameters
    elif a < b:     # ELSE IF a is lower than b
        c = b - a   # then c = b - a
        gcd(a,c)    # gcd is then taking a and c as parameters
    else:           # If two conditionals above invalid, then print a
        print(a)

gcd(350, 80)        # to check 
gcd(5, 1)           

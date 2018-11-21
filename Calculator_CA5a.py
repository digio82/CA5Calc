#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:04:55 2018

@author: FabioDiGiovine
"""

#import math package
import math
from functools import reduce

#create Class Calculator  
class calculator():
    
    # create menu function (use of new line|n )
    def menu():
        print('')
        print ('********************** MENU ********************')
        print('')
        print(' 1 Addition of 2 lists with 4 numbers\n 2 Subtraction of 2 lists with 4 numbers\n 3 Multiplication of 2 lists with 4 numbers\n 4 Division of 2 lists with 4 numbers\n 5 Calculate Max value in a list of 4\n 6 Calculate Min value in a list of 4\n 7 Return even numbers in a list of 4\n 8 Return odd numbers in a list of 4\n 9 Return the square of a range of numbers\n 10 Return the cube of a range of numbers\n 11 TO QUIT\n')
    
    #function choice thet will ask the use to input an INTEGER value (with exception handling)
    def choice():
        while 1==1: 
            try:
                choice = int(input('************************************************\nMake your choice (between 1 and 10 to do a calculation or any other number)\n************************************************\n: '))
                break
            except:
                print('You must enter a integer value')
        return choice

    #askList function to prompt the user to input a list of 4 integer values
    def askList():
        print('')
        print('***Input 4 numbers***')
        while 1==1:
            try:
                val1 = int(input('Input 1st of 4 integer integer values: '))
                break
            except:
                print('You must enter an integer value')
        while 1==1:
            try:
                val2 = int(input('Input 2nd of 4 integer integer values: '))
                break
            except:
                print('You must enter an integer value')
        while 1==1:
            try:
                val3 = int(input('Input 3rdof 4 integer integer values: '))
                break
            except:
                print('You must enter an integer value')
        while 1==1:
            try:
                val4 = int(input('Input 4th of 4 integer integer values: '))
                break
            except:
                print('You must enter an integer value')
        listSeq = [val1,val2,val3,val4]
        return listSeq
    
    #askList function to prompt the user to input a range of numbers
    def askRange():
        print('')
        print('***Input a range***')
        while 1==1:
            try:
                r = int(input('Input a range of values: '))
                break
            except:
                print('You must enter an integer value')
        return r
      
##series of 10 math functions to be used for calculations using Lambda (map, reduce, filter, 
##list comrehension and generator)
        
    def addition(a,b):
        add = list(map(lambda x,y:x+y, a,b))
        return add

    
    def subtraction(a,b):
        sub = list(map(lambda x,y:x-y, a,b))
        return sub
    
    def multiplication(a,b):
        mul = list(map(lambda x,y:x*y, a,b))
        return mul
    
    #division by zero rule
    def division(a,b):
        if 0 not in b:
            div = list(map(lambda x,y:x/y, a,b))
            return div
        else:
            print ('\n************************************************\nNumber 0 is contained in the 2nd list\nIt is not possible to divide a numbers by zero\n************************************************\n')
      
    def maxValue(a):
        maxVal = lambda a,b: a if (a>b) else b
        return reduce(maxVal, a)
        
    def minValue(a):
        minVal = lambda a,b: a if (a<b) else b
        return reduce(minVal, a)
    
    def evenNumbers(a):
        eveN = filter(lambda x: x % 2==0, a)
        return list(eveN)
    
    def oddNumbers(a):
        oddN = filter(lambda x: x % 2, a)
        return list(oddN)
    
    #
    def square(a):
        squares = [x**2 for x in range(a)]
        return list(squares)

    def cube(a):
        gen_exp = (x*x*x for x in range(a))
        for x in gen_exp:
            return list(gen_exp)
        
        
        
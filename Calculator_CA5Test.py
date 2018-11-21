#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:40:07 2018

@author: FabioDiGiovine
"""
#test file

#import unittest package
import unittest

#use class from Calculator_CA5a
from Calculator_CA5a import calculator

calc = calculator

#create test calss with built in funcions with assigned values to be used for the test
#each function will test a separate calc function from the Calculator_CA5a class
#the result should give no fails
class CalculatorTest(unittest.TestCase):
    
    def testAddition(self):
        list1=[1,2,3,4]
        list2=[5,6,7,8]
        self.assertEqual([6,8,10,12], calc.addition(list1,list2))
    
        
    def testSubtraction(self):
        list1=[1,2,3,4]
        list2=[5,6,7,8]
        self.assertEqual([-4,-4,-4,-4], calc.subtraction(list1,list2))
        
    def testMultiplication(self):
        list1=[1,2,3,4]
        list2=[5,6,7,8]
        self.assertEqual([5,12,21,32], calc.multiplication(list1,list2))
        
    
    def testDivision(self):
        list1=[2,4,6,10]
        list2=[2,2,2,2]
        list3=[1,0,3,5]
        self.assertEqual([1,2,3,5], calc.division(list1,list2))
        self.assertEqual(None, calc.division(list1,list3))
    
    def testMaxValue(self):
        list1=[2,4,6,10]
        self.assertEqual(10, calc.maxValue(list1))
        
    def testMinVal(self):
        list1=[2,4,6,10]
        self.assertEqual(2, calc.minValue(list1))
    
    def testEvenNumbers(self):
        list1=[2,3,4,5]
        self.assertEqual([2,4], calc.evenNumbers(list1))

    def testOddNumbers(self):
        list1=[2,3,4,5]
        self.assertEqual([3,5], calc.oddNumbers(list1))
        
    def testSquare(self):
        range1 = 4
        self.assertEqual([0,1,4,9], calc.square(range1))
    
    def testCube(self):
        range1 = 4
        self.assertEqual([1,8,27], calc.cube(range1))

unittest.main()
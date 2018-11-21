#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:05:03 2018

@author: FabioDiGiovine
"""

#Run File
#Import class from  Calculator_CA5a
from Calculator_CA5a import calculator

calc = calculator

#set choice to 0, promt the menu to the user till right selection is done as per menu choices
choice = 0

while choice !=11: 

    calc.menu()
    choice = calc.choice()
    print ('Choice: ', choice)

    #if choice selection is between 1 and 8 ask the user to input a list of 4 numbers    
    if 1<=choice<=8: 
    
        #ask user to input the 1st list of 4 values
        list1 = calc.askList()
        
        #if the choice selection is <=8 and also <=4 ask user to input the 2nd list of 4 values
        if choice <5:
            list2 = calc.askList()
         
        #addition
        if choice == 1:
            result = calc.addition(list1,list2)
            print ('')
            print ('*************************')
            print('The new list is\n',result)
            print ('*************************')
        
        #subtraction    
        elif choice == 2:
            result = calc.subtraction(list1,list2)
            print ('')
            print ('*************************')
            print('The new list is\n',result)
            print ('*************************')
        
        #multiplication
        elif choice == 3:
            result = calc.multiplication(list1,list2)
            print ('')
            print ('*************************')
            print('The new list is\n',result)
            print ('*************************')
        
        #division
        elif choice == 4:
            result = calc.division(list1,list2)
            print ('')
            print ('*************************')
            print('The new list is\n',result)
            print ('*************************')
        
        #return max value in the list
        elif choice == 5:
            result = calc.maxValue(list1)
            print ('')
            print ('***********************************')
            print('The maximum value in the list is ',result)
            print ('***********************************')
        
        #return min value in the list
        elif choice == 6:
            result = calc.minValue(list1)
            print ('')
            print ('***********************************')
            print('The minimum value in the list is ',result)
            print ('***********************************')
        
        #return even number in the list
        elif choice == 7:
            result = calc.evenNumbers(list1)
            print ('')
            print ('***********************************')
            print ('The even numbers in your list are\n', result)
            print ('***********************************')
        
        #return odd numbers in the list
        elif choice == 8:
            result = calc.oddNumbers(list1)
            print ('')
            print ('***********************************')
            print ('The odd numbers in your list are\n',result)
            print ('***********************************')
    
    #(list comprehension) return the list of square values for a range of numbers    
    elif choice == 9:
        r = calc.askRange()
        result = calc.square(r)
        print ('')
        print ('***********************************************')
        print ('Square number list as per your range selection\n',result)
        print ('***********************************************')
    
    #(generator) return the list of cube values for a range of numbers  
    elif choice == 10:
        r = calc.askRange()
        result = calc.cube(r)
        print ('')
        print ('***********************************************')
        print ('Cube number list as per your range selection\n',result)
        print ('***********************************************')
            
            
         
    #or quit the console
    else:
        exit
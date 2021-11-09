
"""
@Author: Ravina Maudekar
@Date: 2021-08-11 12:00:24
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 12:00:24
@Title : To print the power of 2 

""" 


def printPower() :

  TakeInput = int(input("Enter Number : "))

  i = 1
  while(i<=TakeInput<31) :
       
       powerOfTwo = 2 ** i
       print(powerOfTwo)
       i+=1

printPower()       




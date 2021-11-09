
"""
@Author: Ravina Maudekar
@Date: 2021-08-11 08:24:00
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 12:35:00
@Title : To print the power of two

""" 

def printPower() :

  TakeInput = int(input("Enter Number : "))

  i = 1
  while(i<=TakeInput<31) :
       
       powerOfTwo = 2 ** i
       print(powerOfTwo)
       i+=1
       
printPower()       





"""
@Author: Ravina Maudekar
@Date: 2021-08-11 8:26:00
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 12:24:24
@Title : To print the username with message.

""" 


def printName() :

 UserName = input("Enter the name : ")

 checkLength = len(UserName)

 if (checkLength >= 3) :
          print ("Hello " + UserName + " , How are you?")
 else :
     print ("Username should have atleast three characters")
     printName()



printName()

"""
@Author: Ravina Maudekar
@Date: 2021-08-11 12:00:00
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 12:37:00
@Title : To check the leap year.

""" 



def findLeapYear() :
           
    inputYear = int(input("Enter year  : "))
  
    checkLength = str(inputYear)
    lengthOfYear = len(checkLength)

    if (lengthOfYear >= 4) :
           if inputYear % 100 != 0 and inputYear % 4 == 0 or inputYear % 400 == 0 :
                  print("{} is a leap year".format(inputYear))
           else :
                 print("{} is not a leap year".format(inputYear))
             
    else :
        print("Enter year  again : ")
        findLeapYear()





findLeapYear()               
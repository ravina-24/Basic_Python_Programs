"""
@Author: Ravina Maudekar
@Date: 2021-10-11 9:22:00
@Last Modified by: Ravina Maudekar
@Title : To calculate the ecludean distance between x , y and origin .

"""

import math
try:
    x = float(input("Enter value of x : "))
    y = float(input("Enter value of y : "))
    
    ecludeanDistance =math.sqrt(x*x+y*y)
    print("Ecludean distance  = {} ".format(ecludeanDistance))

except ValueError:
    print("Sorry, you can not enter string value ! ")
     








"""
@Author: Ravina Maudekar
@Date: 2021-10-11 10:06:00
@Last Modified by: Ravina Maudekars
@Title : To find the roots of a equation a*x*x+b*x+c .

""" 

from math import sqrt
import math

try:
    a= float(input("Enter value of a : "))
    b=float(input("Enter value of b : "))
    c = float(input("Enter value of c : "))

    delta = b * b - 4 * a *c 
    sqrtOfDeta= math.sqrt(abs(delta))                  

    if delta > 0:  
        print("Roots are real and unequal")  
        print((-b + sqrtOfDeta) / (2 * a))  
        print((-b - sqrtOfDeta) / (2 * a)) 

    elif delta == 0:  
        print("Roots are real and equal")  
        print(-b / (2 * a))

    else:  
        print("Complex Roots")  
        print(- b / (2 * a), " + i", sqrtOfDeta)  
        print(- b / (2 * a), " - i", sqrtOfDeta)  
except:
    print("Invalid input as you enter string value")
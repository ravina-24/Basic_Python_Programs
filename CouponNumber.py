"""
@Author: Ravina Maudekar
@Date: 2021-08-11 14:26:00
@Last Modified by: Ravina Maudekar
@Title : To find the distinct coupon numbers .

""" 
from array import*
from random import randint
import random
class coupon:
    
    def findDistinctCoupon(self):
     print()

    Num = int(input("Enter the Coupon number : "))  
    set =[]
    
    maxLimit =int(input("Enter max limit : "))
    count = 0
    i=1
    isRepeated = True
    for i in range(Num) :
        
        randomNum = randint(0,maxLimit)
        if randomNum not in set :
              set.append(randomNum)
              count+=1
        elif randomNum in set :
           isRepeated = False    
        else:
            print("Does not contain any distict  number")

    print ("Distinct coupon number {}: ".format(count))
    print(set)


c = coupon()
c.findDistinctCoupon()        
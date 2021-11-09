

"""
@Author: Ravina Maudekar
@Date: 2021-08-11 8:00:24
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 12:00:35
@Title : To print the percentage of head and tail 

""" 
TakeInput = int(input("Enter how many times you want to flip the coin : "))

i =1
countofHeads =0
countofTails =0

while (i<=TakeInput):
        i+=1
      
        import random
        flip = random.uniform(0,1)

        print(flip)
        if (flip<0.5) :
                     print("Tails")
                     countofTails+=1
        else :
             print("Head")
             countofHeads +=1 

PercentageofHeads = (countofHeads *100/TakeInput)
print("Percentage of head = ")
print(PercentageofHeads)

PercentageOfTails = 100 - PercentageofHeads
print("Percentage of tail = ")
print(PercentageOfTails)
                   
                      
"""
@Author: Ravina Maudekar
@Date: 2021-09-11 13:00:24
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-09-11 13:00:24
@Title : To print the prime factors of a number.

""" 

print("Finding the prime factors of a number \n")

Num = int(input("Enter the number : "))
i=2
print("Prime factors are")
while(i<=Num and Num !=0 ) :
    
    if Num%i == 0 :
         print(i) 
         
    i+=1



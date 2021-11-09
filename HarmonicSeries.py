"""
@Author: Ravina Maudekar
@Date: 2021-08-11 9:26:00
@Last Modified by: Ravina Maudekar
@Last Modified time: 2021-08-11 
@Title : To print the sum of harmonic series .


""" 

Num = int(input("Enter Harmonic value of N  : "))

i=1
harmonicseries = 0
print("Harmonic series : ")
while (i<=Num and Num !=0 ) :

    

    print ("{}/{} +".format(1,i) ,end=" ")
   
    harmonicseries =harmonicseries+ 1/i 

    
    i+=1


    


   


print()
print("Sum of harmonic series = {} ".format(harmonicseries) )


     

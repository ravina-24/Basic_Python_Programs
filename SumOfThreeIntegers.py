"""
@Author: Ravina Maudekar
@Date: 2021-09-11 9:26:00
@Last Modified by: Ravina Maudekar
@Title : To find the triplets in which sum of three integers adds to zero .

""" 

try:
    from array import*  
    length =int(input("Enter the length of array = "))
     
    intArray = array('i' ,[])

    for i in range(length):
        values = int(input("Enter the value in array : "))
        intArray.append(values)

    count =0
    for i in range(0,length):

        for j in range(i+1,length):

            for k in range(j+1,length):
                    
                if(intArray[i] +intArray[j]+intArray[k] == 0):
                            print(intArray[i],intArray[j],intArray[k])  
                            count +=1                   
    print("Number of triplets : {}  ".format(count)) 
    
except ValueError :
    print("Sorry, String values are not allowd")
finally:
    print("Triplets program executed")

"""
@Author: Ravina Maudekar
@Date: 2021-09-11 9:26:00
@Last Modified by: Ravina Maudekar
@Title : Print the two dimentional array .

""" 
from array import*
try:
    numberOfRows = int(input("Enter Number of rows : "))
    numberOfColoumn = int(input("Enter number of coloumn : "))
    
    matrix = []
    
    for i in range(numberOfRows):
        a=[]
        for j in range(numberOfColoumn):
             elements= int(input("Enter element : "))
             a.append(elements)
        matrix.append(a)
    
    for i in range(numberOfRows):
        for j in range(numberOfColoumn):
            print(matrix[i][j],end = " ")
        print()    


except ValueError:
        print("Invalid input, as you can not enter string")



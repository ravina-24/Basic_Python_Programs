
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
                   
                      
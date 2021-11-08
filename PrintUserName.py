def printName() :

 UserName = input("Enter the name : ")

 checkLength = len(UserName)

 if (checkLength >= 3) :
          print ("Hello " + UserName + " , How are you?")
 else :
     print ("Username should have atleast three characters")
     printName()



printName()

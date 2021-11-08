def findLeapYear() :
           
    inputYear = int(input("Enter year  : "))
  
    checkLength = str(inputYear)
    lengthOfYear = len(checkLength)

    if (lengthOfYear >= 4) :
           if inputYear % 100 != 0 and inputYear % 4 == 0 or inputYear % 400 == 0 :
                  print("{} is a leap year".format(inputYear))
           else :
                 print("{} is not a leap year".format(inputYear))
             
    else :
        print("Enter year  again : ")
        findLeapYear()





findLeapYear()               
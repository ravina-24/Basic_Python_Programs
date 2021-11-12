"""
@Author: Ravina Maudekar
@Date: 2021-08-11 8:26:00
@Last Modified by: Ravina Maudekar
@Title : To perform the stopwatch program and find the elapsed time .

""" 

class watch:

    def findElapedTime(self):
       print()

    startTime = float(input("Enter startTime : "))
    endTime = float(input("Enter end time "))
    
   #calculating hour
    hour = endTime - startTime

    #calculating time in minutes
    startMin = startTime * 60
    endMin = endTime * 60
    min = endMin - startMin

    #claculating time in seconds
    startSec = startTime *3600
    endSec = endTime *3600
    sec = endSec - startSec

     #calculating time in milliseconds
    startMilliSec = startTime*3600*1000
    stopMilliSec = endTime *3600*1000
    milliseconds = stopMilliSec - startMilliSec
           
    print("Elapsed Time : {}:{}:{}:{} ".format(hour,min,sec,milliseconds))
        
obj = watch()
obj.findElapedTime()

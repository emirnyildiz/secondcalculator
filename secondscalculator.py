#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 22:31:31 2021

@author: emirnuriyildiz
"""

"""
Seconds Calculator
1. Write a program that asks the user to enter the current time.
2. Time information should be received as three integer values for hour, minute,
 second. Assume that the input is always numeric in 24 hour format.
3. The program should check whether the input values are within limits: 
    0<= hour <= 23; 0<= minute <= 59 ; 0<= second <= 59
4. Next, the program should ask the user for time difference in seconds. 
You can assume that the time difference will be small, so that the final
 time is not passed midnight.
5. The program should return the final time by adding the time 
difference to the current time and display the final time in military format.
Ex 1: Current time: 11:30:23; Time difference: 3728; Final time: 12:32:31
"""


while True:
    
    print("""The time entry will be made in the form of hours:minutes:seconds.
The time to be added will be entered.
Time: If you enter -1, the system will shut down. """)
     
    a = int(input("Enter hours:"))
    
    if(a == -1):
        print("System Closed.")
        break
    
    b = int(input("Enter minutes:"))
    c = int(input("Enter seconds:"))
    
    
    
    if a <= 23 and b <= 59 and c <= 59:
        
        print("Time you entered:: {}:{}:{}".format(a,b,c))
        
        x = a*3600+b*60+c  
        
        d = int(input("Time to add (s):"))
            
        if (x+d) // 86400 != 0:
               
               kalan1 = (x+d) % 86400
               
               bolum1 = kalan1//3600
               
               kalan2 = kalan1 % 3600
               
               bolum2 = kalan2 // 60
               
               kalan3 = kalan2 % 60
               
               
               print("{}:{}:{}".format(bolum1,bolum2,kalan3))
               
               
        elif ((x+d) // 86400 == 0):
                
                bolum3 = (x+d) // 3600
               
                kalan4 = (x+d) % 3600
               
                bolum4 = kalan4 // 60
               
                kalan5 = kalan4 % 60
                
              
                print("Time added: {}:{}:{}".format(bolum3,bolum4,kalan5))
                
        else:
                
                print("You have entered incorrectly.")
         
    else :
        
        print("You have entered incorrectly. Please, Try Again.")
       
        
        








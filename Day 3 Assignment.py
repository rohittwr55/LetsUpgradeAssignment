# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:35:54 2020

@author: nitish
"""

#Assingnment 2 
#Day 3 
#---------------------------------------------------------
# Part 1
altitude=int(input("Enter the altitude for landing the plane"))
if altitude <=1000:
    print("Land the plane")
elif altitude>1000 and altitude <=5000:
    print("Come down to 1000 ft")
else:
    print("Go around and try again later")
    
#---------------------------------------------------
#Part 2
print("Prime Number between 0-200")
lower = 0
upper =200
for x in range(lower,upper+1):
    if x>=1:
        for i in range(2,x):
            if (x%i) == 0:
                break
        else:
            print("Number",x,"Is prime")
                    
    else:
        print("Number",lower," is less than 1 so it is not a prime")
    
        
        
    
         
         
                
                
    
        
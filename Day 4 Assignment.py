# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:33:44 2020

@author: nitish
"""


for arms in range(1042000,702648265):
    digit=arms
    u=0
    while digit!=0:
    
        x=digit%10
        u=u+1
        digit=digit//10
    y=0
    temp=arms
    while temp!=0:
        x=temp%10
        y=y+x**u
        temp=temp//10
        
    if y == arms:
        print("Number",arms,"Is Armstrong")
        break
    
        
    

   
    
    
        

    



# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:41:30 2020

@author: nitish
"""
#Assinment Day 5
#Assinment 1

def checkLists():
    num=0
    for sublist in sub_list :
        for lst in listy:
            if sublist == lst:
                num = num+1
                break
    if length == num:
        print("It is a match")
    else:
        print("It is Gone")
        

sub_list =[1,1,5]
length = len(sub_list)
listy=[1,5,6,4,1,2,3,5]
checkLists()

#Assinment 2
# Prime number using Filter
def prime(num):
    if num>1:
        for y in range(2, num):
        
            if num % y == 0:
                return False
        else:
            return True
        
lst2=filter(prime,range(2,100))
print(list(lst2))

#Assinment 3
#Use of lambda function
lst=["hey i am sai","i am in mumbai","this is pyhton assinment 3 day 5"]
lst2=map(lambda nameCaptial:nameCaptial.title(),lst)
print(list(lst2))



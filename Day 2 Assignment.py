# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 09:36:56 2020

@author: nitish
"""
#--------------------------------------
#List And their default functions
lis=[1,2,"Rohit"]
print("Lists",lis)
lis.append("Tiwari") #Adding new element
print(lis)
print(lis.count("Rohit")) #counting particular number
lis.reverse() #Reverse a string
print(lis)
lis.insert(1,"Mukesh") #to insert eelemet at particular index
print(lis)
lis2=lis.copy() #Copy list to another list
print(lis2)
lis2.extend(["Suresh"]) #To use of extend method
print(lis2)
lis2.remove("Tiwari") #To remove Particular element
print(lis2)
lis2.clear() #To use clear method
print(lis2)
lis2=[1,2,3,4]
lis2.remove(2) #To use remove method
print(lis2)
lis2.pop(2) # To use remove method
print(lis2)
#---------------------------------------
#Dictionary
dic={"Name":"Rohit","Age":24,"Degree":"MCA"} #Dictionary
print("Dictionaru 1",dic)
dic2=dic.copy() # Copy method
print("Dictionaru 2",dic2)
dic2["Height"]= 5.5 #Add new Item
print(dic2)
dic2["Name"]="Rohit Tiwari" # Updating perticular item
print(dic2)
del dic2["Height"] #Deletig particular item
print(dic2)
del dic2 #Deleting A dictionary
#-----------------------------------------
#Sets
#Defining Sets
st={"Rohit","Letsupgrade","Rohit","Letsupgrade",1,2,3}
print("Sets" ,st)
st.add("Hello") #Add element
print(st)
st2=st.copy() #copy Method
print("Sets 2",st2)
st2.update(["Tiwari","Python"]) #Update Method
print("Set2", st2)
st2.remove("Tiwari") #Remove a particular item
print("Set2",st2)
st3=st.union(st2) #USe of Union method
print("Set 3", st3)
st4=st.intersection(st2) #Intersection
print(st4)
#------------------------------------------
#Tupple
tup=("Rohit","Tiwari",410)
print("Tupple",tup)
x=tup.count(410) #Count
print(x)
#-------------------------------------------------
#String and Default method
name="Rohit tiwari is my name"
n=name.capitalize() #conver First leter to capital letter
print(n)
n=name.count("m")# To count number of word alphabet
print(n) #To find the word at perticular index
n=name.index("tiwari")
print(n)
n=name.lower() #To conver the letter to lower case
print(n)
n=name.upper() #To conver the letter to Upper case
print(n)
















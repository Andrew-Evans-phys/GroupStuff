#imports
from Definitions import * #this lets python see all the code from the Definitions.py file.


###Setup###
#To run python code you will need to download python for your computer 
#Link to download: https://www.python.org/downloads/

#You will also need to edit code in some sort of IDE, I suggest visual studio code
#Link to download: https://code.visualstudio.com/download

#If you want to run this code without downloading anything there exist online 
# python editors. That being said, you will need to upload the auxillary files
# (Errors.py & Definitions.py) to run this file.
#I recommend using the following website if you choose to run the code online
#Link to online IDE: https://www.online-python.com/


###Tutorial###
#A useful resource for python coding is: https://www.w3schools.com/python/
#The side bar on this webpage allows you to select different tutorials in python. 
#Most anything you want to know about python will be on this site.

#comments in python are any characters following #

#to output text to the terminal
#print("Group theory is neat!") #uncomment start of line and run code for print 

#important note, python is whitespace sensitive, in otherwords spaces and tabs matter.
#this will become more important if you want to use functions.

#python is an object oriented language. This means that you can define "objects" (classes)  
# that carry some information with them and "rules" (methods) on these objects

#In this project I created an object that represented a finite group and then build rules
# on these objects to explore topics from our course

#to create a group you must give a list of elements and a function to the group object
#elements = [0,1,2,3]
#def addition_mod_four(a,b): #def is the function definition keyword
   #return (a+b)%4 #the % is the mod operator in python
#G = Group(elements, addition_mod_four)

#now that G has been defined we get to use all the rules that have been definied on 
# groups (these rules are called methods).
#the rules I have defined on groups are:

#ab = G._operation(a, b) #takes in two group elements (a and b) and returns ab
#print(ab) #uncomment to display ab

#a_inv = G.inverse(a) #takes in an element (a) and returns its inverse
#print(a_inv) #uncomment to display a_inv

#order_of_a = G.e_order(a) #takes in an element and returns its inverse
#print(order_of_a)

#a_to_n = G.power(a,n) #takes in an element and raises it to n
#print(a_to_n)

#list_of_powers_of_a = G.powers_of_(a) #takes and element and returns <a> as a list
#print(list_of_powers_of_a)

#G.latex_cayley_table() #prints the Cayley table in latex form

#I have taken the time to define functions that return preset groups. I found 
# that typing each element and operation and then passing that information to  
# Group(elements, function) was too tedious. The following list is all the 
# initialization functions:

#n = 5
#G = init_Z_(n) #makes G into Z_n
#G = init_U_(n) #makes G into U_n
#G = init_D_(n) #makes G into D_n
#G = init_S_(n) #makes G into S_n

#The EDP can be taken on a list of groups via:

#some_list_of_groups = [init_Z_(n), init_U_(n)] #the list length is arbitrary
#new_group = EDP(some_list_of_groups)

#Hopefully this tutorial will give you enough information to play around with 
# the package I build :)
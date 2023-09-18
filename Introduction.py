#This is a comment

#To create a block comment, use quote marks

"""
Here is a block comment
it takes up two lines
"""

'''
Here is another block comment 
using a series of three single quotes 
'''

'''
A Variable - assign values and put them in computer memory 
Asssigning values that are held on to throughout the code 
IE - myvar = 5
Variable names: 
- No spaces 
- Never start with a number (but you can use them in your variables)
- Do not use special characters (you can use _ underscores)
'''

myvar = 5
print(myvar)


'''
String --> text "Hello World" or "5" (will be in quotations) 
Integer -->  5 (a number)
Float --> 5.12 (a number with a decimals)
Boolean --> True or False (must be capilized). Can use 1 and 0(will be interpreted as integers) 
'''

LilyAge = (19)
print(LilyAge)

FavNum = (26)
print(FavNum)

Hanne = ("Hanne is the GOAT")
print(Hanne)

num1 = 2
num2 = "8"

#result = num1 * num2
#result = num1/num2 # Varible reassignment
#result2 = num1/num2
#print(result) Creates a Traceback error because the varibale does not exist
# print(result2)

name = "Hannelore the Great"
#it has to be in quotes because its a string. Text cannot be a float/interger/boolean
address = '69 Ur Moms St'
# you can use double quotes and single quotes and they work the same
title = "Book = 'Python Programming'"
#nesting quote marks ---> quotes within quotes that are printed with the string
age = 22 # integer data type

print(name + "is" + str(age) + " years old") # Mixing string with Variable output
# Cannot mix string and integer data
#concatenator combines data types

#print()
#str() ---> converts integer data type to string
#int() ---> converts a string data type to an integer
#len() ---> returns the total number of characters in a variable
#float() ---> converts integers(includes strings) into a float
#input() ---> allows for user input

#print(name,"is",age,"years old")
# a comma is not a mathematical function so there will be no traceback error
# a comma is a concatenator
# command is better for combing data types

#first_name = input("Enter your name:")
#n1 = input("Enter your first number:")
# n1 = int(input("Enter your first number:"))
#n2 = input ("Enter your second number:")
#n3 = int(n1) + int(n2)
#n2 = int(n2)
# putting int makes the inputs read as integers, this being able to conduct mathematical equations with them
# without this variable defined, the program would just put 2 + 4 as 24
# print("Wassssup", first_name, "The addition of these numbers equals", (n3))

# = len(title)
#print("The number of characters in the variable 'title' equals:", length)
# the quotes to define a string are counted as characters and so are the spaces

grade1 = 3.75
grade2 = 3.25
grade3 = 3.01
grade4 = 3.0
grade5 = 0
courses = 5
statement = "The average GPA equals"
avg = ""

grade5 = input("What is the value of your 5th grade?")

avg = (grade1 + grade2 + grade3 + grade4 + float(grade5))/5
print(statement, avg)

#this is an alternative way to do it
#or sum = grade1 + grade2 + grade3 + grade4 + grade5
# avg sum/courses
#print(statement, avg)







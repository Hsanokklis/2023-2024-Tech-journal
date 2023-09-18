# Working with user defined functions

"""
Function notes:
- What is a function ---> to allow you to pull together realted code that preforms a specific purpose, that you control its execution

- naming is the same as variables (specific as possible)
- must start out with key work "def" and must always be lowercase
- Must end with a full colon

def test_function():
def TestFunction():

- the cursor will be indented when you press enter after defining the fucntion
-  key word "pass" (not ready to enter code, just want to not have kick backs)
- pass --> a place holder so as to keep the interpreter from recognizing an error

Document every function, and its purpose!

Global variable
- a varibale deifined outside a function
- is avaiable to all functions in your file

Local variable:
- a varibale found within a function
- avaibale only in the function

loop:
 - a certain number of steps we want repeated a specified number of times

"""
def test_function():
    pass

# if you were still in the function, when you hit enter after pass, it would still be indented and not in the margin

def PrintText():
    print('Here is some string')
    x = 1
    print('the value of x equals', x) #comma is the concatenator!
    y = 3
    z = x + y
    print(z)

    # MAINTAIN INDENTATION OR DIE

# PrintText() #This is a function call

z = ""
x = 1 # this is refered to as a global variable
y = 0
h = 26
def var_mgt():
    global x # your changing he value of the global variable
    print('Here is some string')
    x = x + 1  # the defined x here is a local variable, the x has to be defined before you call it!
    print('the value of x equals', x) #comma is the concatenator!
    yy = 3 #this is a local variable that is defined within this function, and it will be 3 in the context of this function but no where else
    yy = yy + 3
    zz = x + yy
    print("the value of z equals", zz)
    print("the value of the h variable is", h) # h is a global variable outside the function and it has been called within it!


var_mgt()

#def x_value():
    #global x #global variables have to be defined first
    #print (x)
    #x = x - 1
    #print(x)



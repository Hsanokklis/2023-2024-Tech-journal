# Working with conditional statements

def ChooseOne():
    x = int(input("Enter an integer value for x:"))
    #print("the original value of x equals",x)
    y = 2
    if (x == 0):
        print('The original value of x  equals',x)
        x = x + 1
        print('The value of x now equals',x)
    elif(y == 2): #this will not execute, because the if statement is true. If the if statement was false then it would go to the elif
        print("the value of 'y' equals",y )
    else:
        print("The condition failed, y =", y)


# you can never tie a condition to an else

# ChooseOne()

def MultiConditions():
    name = input('Enter your name:')
    print("please enter '1', '2', '3', or '4' to the quesiton below")
    year = input('What year are you at Champlain College?')
    if(name == "" or year == ""):
        print("Please enter your information")
    else:
        print("Welcome")

MultiConditions()

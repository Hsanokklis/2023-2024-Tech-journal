#Using 'return' in a function

def calc1():
    x = 1
    y = 2
    z = x + y
    print("This is from the calc1 function", z)

def calc2():
    x = 1
    y = 2
    z = x + y
    return z # the result of the operation is held in memory. The function calls results
             # in the ANSWER becoming available for use

calc1()
print(calc2()*5)
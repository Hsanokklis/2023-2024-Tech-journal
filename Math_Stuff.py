# Working with the math module

import math

# using ** is like using exponents ie 2**3 is the same as 2^3
x = 2**3
y = 5**4
#rint(x)
#print(y)

my_pi = 22/7
real_pi = math.pi #pulling pi from the math module

#print(my_pi)
#print(real_pi)

exp = math.pow(1.5,2) # The first value is the number, the second value is the exponent
#print(exp)

#Take the square root of 49 and 50

y1 = int(math.sqrt(49)) # making this int prints it as 7 instead of 7.0
y2 = math.sqrt(50)
#print(y1,y2)

bin_num1 = 0b111 #Prefix binary values with 0b
bin_num2 = 0b110111
result = bin_num1 + bin_num2 # binary values added and then converted into a base 10 valueg
result = bin(result) # bin() function will take any base 10 value and turn it into binary
#print(result)

hex1 = 0xfff #hex values are prefixed with 0x
#print(hex1)
base10 = 365
hex2 = hex(base10) # hex() converts a base10 value into a hexadecimal number
#print('The value of', base10, "equals", hex2)

binvalue = bin(base10)
#print("The binary vlaue of", base10, 'equals', binvalue)

#controlling decmial outpur

real_pi = format(math.pi,".12g") #will round down to 11 decimals
real_pi = format (math.pi,".5f") # will have 5 following decimals
print(real_pi)
#Working with lists

x = [] #Empty List

x = ['a', 'b', 3, True]

print(x)
print(x[1])
#print(x[8]) Creates a Traceback because there is no value in this index position

#Working with the 'for' loop
for i in x: #The 'i' is a variable. The Loop will pass a value from the list `x` to `i`
    print(i) #Prints the current value of `i`

length = len(x)
print(length)

myList = [1,2,6,7,9,0,2,4,5]
new_list = x + myList #list concatentaion
print(new_list)

y = new_list[2:5] # asks for a range of output. The output starts with the value in the
                  # Second index position. It includes all values up to BUT DOES NOT INCLUDE
                  # the value of the last index position. This is called a 'slice'.
print("The contents of new_list are:", new_list)
print(y)

#Pulling items from a list based on a negative index value
print(y[-2]) #Goes to the end of list, pulls out the second item from the end of
             #the list
print(myList[-2:-0]) #Starting a slice with a negative value ends up returning an empty list

names = ["john", "sally", "sam"]

names[2] = "chirs" #The value of "sam" was replaced by "chris"

print(names)


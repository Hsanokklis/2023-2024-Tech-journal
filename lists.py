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

names = ["john", "sally", "sam", "Larry", "Mary"]

names[2] = "chris" #The value of "sam" was replaced by "chris"

print(names)

pos = names.index('chris') # The Index method returns the index position of a value in the list.
print(pos)

remove = names.remove("chris") #The remove() will remove an item named in the function. The value
                               #of 'chris' is gone. You cannot pass the value you remove to a variable.
                               #pass the variable to a variable before its removed.
print(names)

del myList[4] # deletes the item according to the index position noted
print(myList)

names.append('sam') #adds the value in the () to the end of the list
print(names)

names.insert(10, 'keith') #This inserts a value at a specific index position in the list
                         #The first value must be the index position and the second value is the item.

print(names)
pos1 = names.index('keith')
print(pos1)

print(myList) #This shows the items as they are in the list
myList.sort()
print(myList) #This shows the sorted list

print(names)
names.sort() #capitalize words come first in the sort
print(names)
names.sort(reverse = True) #preforms a reverse sort
print(names)

names.sort(key = str.lower) #sorts by strict alphabetic rules
print(names)

mixedList = ["john", "sally", "sam", "Larry", "Mary", "1", "2"]
mixedList.sort() #string numbers get sorted first followed by capitalized names followed by lower case names
print(mixedList)




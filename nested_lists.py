"""

# Working with nested lists

number_sequence = [
    0, 1, 2, 3
]

#print(number_sequence)

#nested_num_list is an example of a nested list or a list within a list =
nested_num_list = [
    [1, 2, 3], # index position 0
    [4, 5, 6], # index position 1
    [7, 8, 9], # index position 2
    [0]
]

print(nested_num_list[1])
# The interpreter treats nested lists in a row first, column second order
print(nested_num_list[1][2])

"""

# 2 examples of lists
#the bad_nested_list makes it harder to visualize the rows and columns of the list
bad_nested_list = [["a", "b"], ['z', 's', 'w'], ['q', 'e']] # icky

good_nested_list = [
    ["a", "b"],
    ['z', 's', 'w'],
    ['q', 'e']
]
better_list = [] # created an empty list
for i in good_nested_list:
    for j in i: # pass each individal item to i
        better_list.append(j) # put the items in the list

    better_list.sort()
    print(better_list)

# Nested for loop
"""
for i in nested_num_list: # This passes each nested list to i
    for j in i: # This passes each individual item in each list to j
        print(j)
"""



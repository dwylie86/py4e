# Concatenate lists using + operator
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Lists can be sliced using colon (:) The second number is up to, but not including.
t = [9, 41, 12, 3, 74, 15]
print(t)
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

# List methods include: 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort'
list_dir = list()
print(dir(list_dir))

# Here's how to build a list from scratch. .append will add items to the end of a list.
scratch_list = list()  # List with an empty constructor
scratch_list.append('book')
scratch_list.append(99)
print(scratch_list)
scratch_list.append('cookie')
print(scratch_list)

# Using 'in' to find something in a list. Returns Boolean True or False. This doesn't modify list
search_list = [1, 9, 21, 10, 16]
print(9 in search_list)
print(15 in search_list)
print(20 not in search_list)  # Using a negative to see if something is not in the list

# List are maintained in order, you can use methods to change the order permanently
friends = ['joseph', 'glenn', 'sally']
print(friends)
friends.sort()  # List sorts itself
print(friends)

# Built in funcions for lists
number_list = [3, 41, 12, 9, 74, 15]
print(len(number_list))  # How many elements are in list
print(max(number_list))  # Largest element in list
print(min(number_list))  # Smallest element in list
print(sum(number_list))  # Sums all list elements
print(sum(number_list) / len(number_list))  # The average value of elements in a list.

# Creating a loop to take in user inputs and get an average
numlist = list()  # Make Empty List
while True:
    inp = input('Enter a Number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print(f'Average is: {average}')

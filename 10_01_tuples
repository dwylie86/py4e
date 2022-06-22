# Set up similarly to lists but use parentheses instead of brackets.
# They are immutable, meaning parts cannot be modified, however, the entire Tuple can be modified.
# You cannot sort, append, reverse, extend, insert, pop, or remove tuples
# Tuples are more efficient than lists, the tuple is not modifiable and Python allocates less resources.
# This make tuples perfect for temporary variables.
x = ('glenn', 'sally', 'joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

for iter in y:
    print(iter)

# You can count and index a tuple
t = tuple()
print(dir(t))


# Tuples can be used on both sides of an assign statement.
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print((a))

# The .items brings returns the key-value pairs as tuples
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():
    print(k, v)

tups = d.items()
print(tups)

# Tuples are comparable
(0, 1, 2) < (5, 1, 2)

# You can sort dictionaries after grabbing their tuples and using .sorted function
# It only sorts by the key (first item) in the tuple.
d = {'a':10, 'c':22, 'b':1}
print(d.items())
print(sorted(d.items()))

# Here's an example building it into a loop and sorting by key
d = {'a':10, 'c':22, 'b':1}
u = d.items()
t = sorted(u)
for k, v in t:
    print(k, v)
# Unsorted Loop
for k, v in u:
    print(k, v)

# Here's an example building it into a loop and sorting by value.
# You have to loop it into a list, swapped, putting the value first.
c = {'a':10, 'c':22, 'b':1}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

# Then you can use sorted and reverse on it.
print(sorted(tmp))
print(sorted(tmp, reverse=True))

# Here's using the assignment from last chapter, and grabbing the top ten words used.
name = input("Enter file:")
fhand = open(name)  # File Handler
counts = dict()  # Empty Dictionary
for line in fhand:  # loops through line and grabs words
    words = line.split()
    for word in words:  # appends the first mention of a word with 0 value, or adds to value in dict
        counts[word] = counts.get(word, 0) + 1

lst = list() # Creates list for us to sort the tuples from the counts dictionary
for key, val in counts.items():  # Since we are sorting by value, need to swap k and v
    newtup = (val, key)  # New tuple defined.
    lst.append(newtup)  # New tuples added to the list

lst = sorted(lst, reverse=True)  # list is sorted by largest value first

for val, key in lst[:10]:  # Loop to flip back to key-value and print the first 10 items in the list
    print(key, val)

# There is a way to cut down the amount of code used when sorting tuples using List comprehension

e = {'a':10, 'c':22, 'b':1}
print(sorted([v,k] for k,v in e.items()))

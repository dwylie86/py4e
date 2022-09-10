# Lists and Definite Loops are best pals!
friends = ['joseph', 'glenn', 'sally']
for friend in friends:
    print(f'Happy New Year, {friend.title()}!')
print('Done!')

# We use index operators to look inside lists
print(friends[1])

# Lists are mutable, you can change contents of a list. Strings are not mutable.
lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 28
print(lotto)

# The len() function will tell you how many elements (items) are in a list.
print(len(lotto))

# The list(range()) functions RETURNS A LIST OF NUMBERS that range from zero to one less than the
# last parameter. We can print our the index numbers instead of elements using it.
# Using the range() function by itself will get you the first and last index parameter.

print(list(range(4)))
print(list(range(len(lotto))))
print(list(range(len(friends))))

# Using range in a for loop will make the iteration go through the index. Produces the same result.
for i in range(len(friends)):
    i = friends[i]
    print(f'Happy New Year, {i.title()}!')
    

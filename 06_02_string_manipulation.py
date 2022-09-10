# String Concatenation
a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)

# Using in as a Logical Operator
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print('Found it!')

# String Comparison. Strings are objects.
word = 'banana'
if word == 'banana':
    print('ALL RIGHT!, bananas!')

word = 'banana'
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('ALL RIGHT!, bananas!')

# Pyton sorts capital letters before lowercase letters, and it's good practice to name all strings in
# lowercase and then change them with methods after the fact.
greet = 'hello bob'
capital_greet = greet.upper()
title_greet = greet.title()
print(greet)
print(capital_greet)
print(title_greet)

print('HI THERE'.lower())

# You can discover what methods an object has in its library by using the 'dir'
stuff = 'string'
print(type(stuff))
print(dir(stuff))

# Use the find() method to search for the first occurrence of substring in a string.
# If the substring is not found, -1 is returned
fruit = 'banana'
pos = fruit.find('na')
print(pos)
zz = fruit.find('z')
print(zz)

# .replace('find', 'replace) example
bob_greet = 'Hello Bob'
replace_bob = bob_greet.replace('Bob', 'Jane')
print(bob_greet)
print(replace_bob)

replace_os = bob_greet.replace('o', 'x')
print(replace_os)
print(bob_greet)

# Stripping Whitespace
wspace_bob_greet = '        Hello Bob    '
print(wspace_bob_greet.lstrip())
print(wspace_bob_greet.rstrip())
print(wspace_bob_greet.strip())

# Prefix example
line = 'Please have a nice day'
print(line.startswith('Please'))
print(line.startswith('p'))
print(line.startswith('P'))

# Parsing and Extracting
data = 'From stephen.marquard@uct.ac.za Sat Jan   5  09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1:sppos]
print(host)
pos = data.find('.')
print(data[pos:pos+3])

x = 'From marquard@uct.ac.za'
print(x[14:17])

print(len('banana')*7)

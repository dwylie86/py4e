# Strings and lists are best friends. The .split method breaks a string into parts and makes a list.
abc = 'With three words'
split_abc = abc.split()
print(abc)
print(split_abc)
print(len(split_abc))
print(split_abc[0])

# Looping through the split string
for word in split_abc:
    print(word)

# .split's default delimeter is white space, however, extra spaces don't matter.
line = 'A lot                    of spaces'
split_line = line.split()
print(split_line)
print(len(split_line))

# You can specify a delimeter to use with .split in the parentheses
line_2 = 'first;second;third'
line_2_split = line_2.split(';')
print(line_2_split)

# Example of splitting up something in a document.
# This example grabs the lines that starts with 'From ' and turns it into a list.
# It then prints our the [2] index, which is the day of the week.
fhand = open('G:\My Drive\python_crash_course\py4e\mbox-short.txt')
for lines in fhand:
    lines = lines.rstrip()
    if not lines.startswith('From '): continue
    words = lines.split()
    dow = words[2]
    email = words[1]
    email_pieces = email.split('@') # This line is a double split pattern, splits the line even further.
    print(dow)
    print(email)
    print(email_pieces)

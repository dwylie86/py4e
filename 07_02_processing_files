# Opening a file. When a file is opened by python, it treats the file like a string, including
# line breaks aka '\n's. That means 'for' loops can iterate through it like a sequence,
# aka an ordered set.
# Print File. This example prints out the file as it is.
# xfile is our file handler.
xfile = open(FILE NAME)
for lines in xfile:
    print(lines)

# Counting lines. This example counts the number of lines in the file.
# fhand is our file handler
fhand = open(FILE NAME)
f_line_count = 0

for lines in fhand:
    f_line_count += 1
print(f'Line Count: {f_line_count}')

# The .read() method converts the file into one big line string.
rhand = open(FILE NAME)
single_string = rhand.read()
print(len(single_string))
print(single_string[:20])

# Searching a file. You can search through a file with the .startswith() method
# This example originally prints out blank lines, because print statement adds them.
shand = open(FILE NAME)
for email_line in shand:
    # .rstip() removes the lines from this loop.
    email_line = email_line.rstrip()
    if email_line.startswith('From:'):
        print(email_line)

# You can write this code to loop with the using the opposite. It's a stylistic different
not_shand = open(FILE NAME)
for not_email_line in not_shand:
    not_email_line = not_email_line.rstrip()
    if not not_email_line.startswith('From:'):
        continue  # This is our skip over lines that don't have 'From'
    print(not_email_line)

# We can use 'in' to search in a line for something.
ihand = open(FILE NAME)
for in_line in ihand:
    in_line = in_line.rstrip()
    if '@uct.ac.za' in in_line:
        print(in_line)

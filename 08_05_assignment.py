# This program prints and counts email addresses from a file.
fname = input("Enter file name: ")

fh = open(fname)
count = 0

for lines in fh:
    lines = lines.rstrip()
    if not lines.startswith('From '): continue
    words = lines.split()
    email = words[1]
    print(email)
    count += 1

print(f'There were {count} lines in the file with From as the first word')

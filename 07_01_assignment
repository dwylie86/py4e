# Use words.txt as the file name. This program prints out the file in uppercase
fname = input("Enter file name: ")

try:
    fh = open(fname)

except:
    print(f'Invalid file name: {fname}')
    quit()

for lines in fh:
    lines = lines.rstrip()
    print(lines.upper())
    

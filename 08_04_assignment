fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    words = line.rstrip()
    words = line.split()
    for unique in words:
        if unique not in lst:
            lst.append(unique)
lst.sort()
print(lst)

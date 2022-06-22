# File handler stuff, this checks for an input if no input runs default file as shortcut
name = input("Enter file:")
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)  # File Handler

counts = dict()  # Empty dictionary to our time and count KV Pairs too

# This for loop does:
for lines in handle:
    lines = lines.rstrip()  # Strips out white space
    if not lines.startswith('From '): continue # Skips over lines that don't hav 'From' at the front
    words = lines.split()  # Creates a variable with each word in line split out
    rough_tod = words[5]  # Creates variable that isolates only the time of day at index 5
    tod = rough_tod.split(':')  # This double split pattern isolated each part of the TOD.
    for hour in tod[:1]:  # This loop creates our histogram using the first two digits (Hour)
        counts[hour] = counts.get(hour, 0) + 1

lst = list()  # Creating and empty list to dump our tuples into

for key, val in counts.items():  # Loop to populate a list to sort
    newtup = (key, val)  # New tuple defined
    lst.append(newtup)  # New tuples added to the list

lst = sorted(lst)  # Sort the list

for key, val in lst:  # Loop to print out results
    print(key, val)
    

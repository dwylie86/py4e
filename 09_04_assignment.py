# File handler stuff, this checks for an input if no input runs default file as shortcut
name = input("Enter file:")
if len(name) < 1:
    name = 'mbox-short.txt'
handle = open(name)  # File Handler

counts = dict()  # Empty dictionary to add our email counts to

# This for loop does:
for lines in handle:
    lines = lines.rstrip()  # Strips out white space
    if not lines.startswith('From '): continue # Skips over lines that don't hav 'From' at the front
    words = lines.split()  # Creates a variable with each word in line split out
    rough_email = words[1]  # Creates variable that isolates only the email address at index 1
    emails = rough_email.split()  # This double split patter cleans up the email address.
    # This loop uses a counting idiom to populate our dictionary with key with empty values.
    for email in emails:
        counts[email] = counts.get(email, 0) + 1  # This counts each time an email is present

big_email = None  # Variable for the email with largest count
big_count = None  # Variable for the largest value count

# Loops through each key-value pair in the dictionary and stores the pair with the largest value.
for key, value in counts.items():
    if big_email is None or value > big_count:
        big_email = key
        big_count = value

print(big_email, big_count)

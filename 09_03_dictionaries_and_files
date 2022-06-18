# The general pattern to count the words in a line of text is to split the line
# into words, then loop the words and use a dictionary to track the count of each word.
counts = dict()  # Create an empty dictionary
print('Enter a line of text: ')
line = input('')  # Type in a line of text

words = line.split()  # Line get's split up into individual words

print(f'Words: {words}')

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1  # This is an idiom we use to count in dictionaries
print(f'Counts: {counts}')

# Even though dictionaries are not stored in order, we can write a for loop that goes through all
# the entries in a dictionary. When it does this, it actually goes through all the keys in dictionary
# and looks up the values.

# Here's an example of retrieving the keys AND values aka key-value pairs (.item method)
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj.items())
# Here's an example of retrieving just the keys (.keys method)
print(jjj.keys())
# or just the keys using list function
print(list(jjj))
# Here's an example of retrieving just the values (.values method)
print(jjj.values())

# We can loop through thge key-value pairs using TWO iteration variables in the for loop.
# Each iteration: The first variable is the key, the second is the corresponding value
jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for key, value in jjj.items():
    print(f'{key} {value}')

# Here's the program we saw in chapter 1 of the books, we have the knowledge to understand it!
name = input('Enter file: ')  # Usre input
handle = open(name)  # Our file handler

counts = dict()  # Creates and empty dictionary for use to add key-value pairs
for line in handle:  # Start of our loop
    words = line.split()  # Makes each word in the string and individual word
    for word in words:
        counts[word] = counts.get(word, 0) + 1  # This idiom adds the word with 0 value, adds one each time

bigcount = None # This will be the Value in the dictionary with the largest value
bigword = None # this will be the Key in the dictionary with the largest value
for word, count in counts.items():  # this loop goes through each key-value pair in counts dictionary
    if bigcount is None or count > bigcount:  # This keeps the key-value pair with the largest value
        bigword = word
        bigcount = count

print(f'Word most used: {bigword.title()} ({bigcount} times)')

fruit = 'banana'
letter = fruit[1]
print(letter)
print(len(fruit))

x = 3
w = fruit[x - 1]
print(w)

# Example of while loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# Example of for loop
index = 0
for letter in fruit:
    print(index, letter)
    index += 1

# Looping and Counting Reminder
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(f'Number of \'{letter}\'s in {word}: {count}')

# Slicing Strings. Separated by colon, if the end number is passed the actual end, slice will stop at end.
s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(len(s))

# You can eliminate the left and right of the range if you are starting at the beginning and stopping at end
print(s[:5])
print(s[6:])
print(s[:])

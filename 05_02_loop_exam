# This program prompts the user to enter numbers until they type in 'done' if the user inputs anything but an integer, an error is given and the loop continues. 
largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == 'done':
        break
    try:
        inum = int(snum)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = inum
        continue
    if smallest is None:
        smallest = inum
        continue
    if inum > largest:
        largest = inum
        continue
    if inum < smallest:
        smallest = inum
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

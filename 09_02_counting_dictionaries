# Historgram Exercise with dictionaries
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Looping through dictionary to count occurances.
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# Python has a get method that does the previous function
# Simplified counting with .get
get_counts = dict()
get_names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for get_name in get_names:
    get_counts[get_name] = get_counts.get(get_name,0) + 1 # This line combines the if and else statements
print(get_counts)

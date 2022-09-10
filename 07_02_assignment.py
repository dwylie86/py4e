# Use the file name mbox-short.txt as the file name. This program searches a file for spam emails, sums the confidence number, and returns the average at the end.
fname = input("Enter file name: ")

try:
    fh = open(fname)

except:
    print(f'Invalid file name: {fname}')
    quit()

count = 0
running_total = 0.0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        colon_pos = line.find(':')
        after_colon_chunk = str(line[colon_pos + 1:])
        float_number = float(after_colon_chunk)
        running_total += float_number
        count += 1
print(f'Average spam confidence: {running_total / count}')

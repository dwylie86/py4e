# My Example
text = "X-DSPAM-Confidence:    0.8475"
numpos = text.find('0')
numstring = text[numpos:]
floatnum = float(numstring)
print(floatnum)

# Actual Solution
text = "X-DSPAM-Confidence:    0.8475"
colon_pos = text.find(':')
after_colon_chunk = str(text[colon_pos+1:])
float_number = float(after_colon_chunk)
print(float_number)

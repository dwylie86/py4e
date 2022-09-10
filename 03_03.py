# This code will tell you what your grade is when you enter a value between 0.0 and 1.0
score = input("Enter Score: ")

try:
    s = float(score)
except:
    print("Enter a numeric value between 0.0 and 1.0")
    quit()

if s < 0.6:
    grade = "F"
elif s < 0.7:
    grade = "D"
elif s < 0.8:
    grade = "C"
elif s < 0.9:
    grade = "B"
elif s <= 1.0:
    grade = "A"
else:
    print("Enter a numeric value between 0.0 and 1.0")
    quit()
print(grade)

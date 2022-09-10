# This code uses inputs to determine pay. The Try/Except prevent traceback errors.
hrs = input("Enter Hours: ")
pay = input("Enter Pay Rate: ")

try:
    h = float(hrs)
    p = float(pay)
except:
    print("Enter a numeric input next time")
    quit()

if h > 40:
    rp = h * p
    otp = (h - 40) * (p * 0.5)
    gross_pay = rp + otp
else:
    gross_pay = h * p
print(gross_pay)

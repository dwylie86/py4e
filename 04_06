# This is the same as a previous assignment, but using and invoking a function to calculate gross pay
hrs = input("Enter Hours: ")
pay = input("Enter Pay Rate: ")

try:
    h = float(hrs)
    p = float(pay)
except:
    print("Enter a numeric input next time")
    quit()

def computepay():
    if h > 40:
        rp = h * p
        otp = (h - 40) * (p * 0.5)
        gross_pay = rp + otp
        return gross_pay
    else:
        gross_pay = h * p
        return gross_pay


output = computepay()
print("Pay", output)

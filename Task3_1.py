hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
h = float(hrs)
r = float(rate)
if h > 40 :
    inc = h - 40
    pay = ((inc * 1.5)+40)*r
else:
    pay = h * r
print(pay)

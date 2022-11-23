def computepay(h, r):
    if h > 40:
        inc = h - 40
        s = ((inc * 1.5)+40)*r
    else:
        s = h * r
    return s

hrs = input("Enter Hours: ")
rate = input("Enter Hours: ")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        k = int(num)
    except:
        print("Invalid input")
        continue
    if largest == None and smallest == None:
        largest = k
        smallest = k
    elif largest < k:
        largest = k
    elif smallest > k:
        smallest = k
print("Maximum is",largest)
print("Minimum is",smallest)

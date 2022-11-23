score = input("Enter Score: ")
conv = float(score)
if conv >= 0.0 and conv <= 1.0 :
    if conv >= 0.9:
        print("A")
    elif conv >= 0.8:
        print("B")
    elif conv >= 0.7:
        print("C")
    elif conv >= 0.6:
        print("D")
    else:
        print("F")
else :
    print("Wrong score")

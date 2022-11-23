fname = input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 2:
        continue
    if wds[0] == 'From':
        print(wds[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")

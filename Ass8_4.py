fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    wds = line.split()
    for w in wds:
        if w in lst:
            continue
        else:
            lst.append(w)
gh = sorted(lst)
print(gh)

name = input("Enter file: ")
handle = open(name)
words = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 2:
        continue
    if wds[0] == 'From':
        email = wds[1]
        words[email] = words.get(email,0) + 1
file = None
counts = 0
for word,count in words.items():
    if count is None or count > counts:
        file = word
        counts = count
print(file,counts)

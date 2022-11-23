name = input("Enter file: ")
handle = open(name)
words = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 2:
        continue
    if wds[0] == 'From':
        time = wds[5]
        tim = time.split(":")
        hour = tim[0]
        words[hour] = words.get(hour,0) + 1
lst = list()
for hour, count in words.items():
    arr = (hour, count)
    lst.append(arr)
lst = sorted(lst)
for hour, count in lst:
    print(hour,count)

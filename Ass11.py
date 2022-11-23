import re
name = input("Enter file: ")
handle = open(name)
lst = list()
for line in handle:
    line = line.rstrip()
    if re.search('[0-9]+',line):
        num = re.findall('[0-9]+', line)
        for i in num:
            i = int(i)
            lst.append(i)
    else:
        continue
Sum = sum(lst)
print(Sum)

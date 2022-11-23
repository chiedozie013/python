# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
jh = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    gh = line.find('0')
    hh = line[gh :]
    ih = float(hh)
    jh = jh + ih
kh = jh / count
print("Average spam confidence:",kh)

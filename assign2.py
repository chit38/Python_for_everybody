# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0 
count=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos=line.find('0')
    val= line[pos:]
    count = count + 1
    total = total + float(val)
    #print(line)
ans= total/count
print('Average spam confidence:', ans)
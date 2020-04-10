fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
dct=dict()
for line in fh:
    if line.startswith("From"):
        if line.startswith("From:"): continue
        temp = line.split()
        test=temp[1]
        dct[test] = dct.get(test, 0) + 1
        count= count +1
#print("There were", count, "lines in the file with From as the first word")
mail = None
ans = None
for key,val in dct.items():
    if mail is None:
        mail= val
        ans = key
    elif val>mail:
        mail= val
        ans = key
print(ans, mail)
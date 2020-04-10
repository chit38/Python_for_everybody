fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0
time= dict()
for line in fh:
    if line.startswith("From"):
        if line.startswith("From:"): continue
        temp = line.split()
        hr=temp[5].split(':')[0]
        time[hr]= time.get(hr,0) + 1
        
lst =sorted([(v,k) for v,k in time.items()]) 
for h,t in lst:
    print(h, t)
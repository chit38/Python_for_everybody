import re
fname = input("Enter file name: ")
fh = open(fname)
final_list = list()
for line in fh:
    temp = re.findall('[0-9]+', line)
    if len(temp)>0:
        for num in temp:
            num=int(num)
            #print(num) 
            final_list.append(num)

print(sum(final_list))
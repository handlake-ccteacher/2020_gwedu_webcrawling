import csv
import json

llist = []
with open('lotto_original.csv', 'r') as f:
    m = csv.reader(f)
    for n in m:
        llist.append(n)
lottodata=[]
#print(len(llist))
#print(llist[3])
for i in range(3, 935):
    dlist = [llist[i][1]]
    for n in range(13,20):
        dlist.append(llist[i][n])
    lottodata.append(dlist)
ljson=[]
for data in lottodata:
    tdict = {'times':data[0]}
    for i in range(1, 7):
        tdict[f'{i}']=data[i]
    tdict['bonus'] = data[7]
    ljson.append(tdict)

json.dumps(ljson, indent=4)


with open('lottorawdata.json', 'w', encoding='utf8') as f:
    json.dump(ljson, f)

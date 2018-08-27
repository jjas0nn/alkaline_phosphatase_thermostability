from process_csv import *
from collections import defaultdict
import csv
import requests
with open("dataset/dataset.csv") as file:
    reader=csv.reader(file)
    data=list(reader)
header=data[0]
i=0
j=1
csvdict={}
while i<len(data[j]):
    csvdict[header[i]]=[]
    while j<len(data):
        csvdict[header[i]].append(data[j][i])
        j+=1
    j=1
    i+=1
for key,val in csvdict.items():
    val=list(map(float, [a for a in val if a]))
    csvdict[key]=val
print(csvdict)

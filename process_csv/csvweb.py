import csv
import codecs
import requests
import urllib.request
url='http://jj-jj.xyz/dataset/ap_26012018.csv'
response=requests.get(url)
csvfile=csv.reader(response.text.strip().split('\n'))
data=[]
for line in csvfile:
    data.append(line)
print(data)

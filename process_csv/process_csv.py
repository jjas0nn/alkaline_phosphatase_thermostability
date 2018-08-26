import csv
from collections import defaultdict
import pandas as pd
import scipy
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.misc import derivative
class process_csv:
    def __init__(self, file):
        with open(file) as csvfile:
            self.reader=csv.reader(csvfile)
            self.data=list(self.reader)
        self.header=data[0]
    def get_header(self):
        return self.header
    def csv2dict(self,header_item):
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
        return csvdict
    def get_sum(self,array):
        i=0
        sum=0
        while i<len(array):
            sum=sum+array[i]
            i+=1
        return sum
    def mod_header(self):
        new_list=[]
        for item in self.header:
            if "2018" not in item and "time" not in item:
                new_list.append("23072018t"+item)
        return(new_list)
    def transform(self):
        #scale data points
        scaler=MinMaxScaler()
        print(scaler.fit(self.csv2pair()))
        MinMaxScaler(copy=True, feature_range=(0,1))
        return scaler.transform(self.csv2pair())
    def locf_helper(self,x,y):
        xlength=len(x)
        ylength=len(y)
        lastval=y[ylength-1]
        while xlength>ylength:
            y.append(lastval)
            ylength+=1
    def plot(self,xlabel,ylabel,legend_label,title):
        self.locf_helper(self.xval,self.yval)
        plt.plot(self.xval,self.yval, label=legend_label)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend()
        plt.savefig('plot.png',bbox_inches='tight')


# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 09:43:41 2022

@author: Alex
"""
#IMPORT LIBRARIES
import pandas as pd
import os as os
#import SetAlgebra as sa
#import SetAlgebra as sa

#DEFINITIONS
myWatchList = (["xom"])
myYear = 2018
myQuarter = "q1"
mySavePath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data test', myWatchList[0] + str(myYear) +myQuarter + ".csv")
numPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data SEC', str(myYear) + myQuarter + r"\num.txt")
subPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data SEC', str(myYear) + myQuarter + r"\sub.txt")
tagPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data SEC', str(myYear) + myQuarter + r"\tag.txt")
num_SEC = pd.read_csv(numPath, sep = '\t')
sub_SEC = pd.read_csv(subPath, sep = '\t')
tag_SEC = pd.read_csv(tagPath, sep = '\t')
#FILTER
#sub_SEC = sub_SEC[sub_SEC.form  == "10-K"]
d1 = dict(zip(sub_SEC.adsh, sub_SEC.cik))
tic_SEC = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data SEC\TickersCIKs2.txt",sep = "\t")
tic_SEC = tic_SEC.drop_duplicates(subset=['cik'])
d2 = dict(zip(tic_SEC.cik, tic_SEC.tic))
num_SEC['cik'] = num_SEC['adsh'].map(d1)
num_SEC['tic'] = num_SEC['cik'].map(d2)
num_SEC = num_SEC[num_SEC.adsh.isin(sub_SEC.adsh)]



num_SEC = num_SEC[num_SEC.tic.isin(myWatchList) == True]

tag_SEC = tag_SEC[['tag', 'tlabel']]
d3 = dict(zip(tag_SEC.tag, tag_SEC.tlabel))

num_SEC['tlabel'] = num_SEC['tag'].map(d3)

num_SEC.to_csv(mySavePath)







# num_SEC = num_SEC[['tag', 'value']]
# read = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data test\match.csv", sep = ',')
# matchy = read[read['2020'].isin(num_SEC['value']) == True]
# matchy.to_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data test\THESEMATCH.csv")
# #matchy['num'] = 


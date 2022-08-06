# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 14:49:36 2022

@author: Alex
"""
import pandas as pd
import numpy as nm
import yfinance as yf
"""
#READ IN CSV DATA TO PYTHON
"""
myData = pd.read_csv(r"C:\Users\Alex\Documents\book3.csv")
myItems = (["Item1","Item2"])
print(myData)
filteredData1 = myData[myData.Item.isin(myItems) == True]
#difference2 = myDF2[myDF2.Col1.isin(myDF1.Col1) == False]
print(filteredData1)

myTicker = "OLN"
myPeriod = "240mo"
myInterval = "1d"
myPath = r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Stock Price Data' + myTicker + '_' + myPeriod + '_' + myInterval + '.csv'

data = yf.download(tickers=myTicker,period='240mo',interval='1d')
print(data)
data.to_csv(myPath)
"""
#WRITE FILTERED DATAFRAME TO ANOTHER FILE
"""
filteredData1.to_csv(r"C:\Users\Alex\Documents\book4.csv")
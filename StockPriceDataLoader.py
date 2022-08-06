# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 08:53:50 2022
@author: Alex
"""
import pandas as pd
import numpy as nm
import yfinance as yf
import os
import time


#STOCK PRICE IMPORT
myTickerList = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Sources\Indices.csv")
#myTickerList = (["Item1","Item2"])

for i in myTickerList.index:
        col1 = pd.Series(myTickerList.Tick)
        myTicker =  col1[i]
        print(myTicker)
        myPeriod = "max"
        myInterval = "1d"
        myFilename = myTicker + "_" + myPeriod + "_" + myInterval + ".csv"
        myPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\Stock Price History',myFilename)
        priceData = yf.download(tickers=myTicker,period = myPeriod,interval = myInterval)
        priceData['SMA_10d'] = priceData['Close'].rolling(10,min_periods=10).mean()
        priceData['SMA_50d'] = priceData['Close'].rolling(50,min_periods=50).mean()
        priceData['SMA_200d'] = priceData['Close'].rolling(200,min_periods=200).mean()
        k = priceData['Close'].ewm(span=12, adjust=False, min_periods=12).mean()
        d = priceData['Close'].ewm(span=26, adjust=False, min_periods=26).mean()
        macd = k - d
        macd_s = macd.ewm(span=9, adjust=False, min_periods=9).mean()
        macd_h = macd - macd_s
        priceData['macd'] = priceData.index.map(macd)
        priceData['macd_h'] = priceData.index.map(macd_h)
        priceData['macd_s'] = priceData.index.map(macd_s)
        #priceData['change'] = priceData['Open'] - priceData['Close']
        priceData['change'] = priceData['Close'].diff()
        priceData['gainVal'] = priceData[priceData[['change']]>0].change.fillna(0)
        priceData['gainVal'] = priceData['gainVal'].abs()
        priceData['lossVal'] = priceData[priceData[['change']]<=0].change.fillna(0)
        priceData['lossVal'] = priceData['lossVal'].abs()
        priceData['avgGain'] = priceData['gainVal'].ewm(com = 13,min_periods=14).mean()
        priceData['avgLoss'] = priceData['lossVal'].ewm(com = 13,min_periods=14).mean()
        priceData['RSI1'] = priceData.avgGain/priceData.avgLoss
        priceData['RSI2'] = 100 - (100/(1+priceData.RSI1))
        
        priceData.to_csv(myPath)
        time.sleep(3.2)
#macd_h = convergence/divergence in StockMaster -validated
#macd_s = signal in StockMastr
# =============================================================================
# #BALANCE SHEET IMPORT
# for i in myTickerList.index:
#        # print(i)
#        col1 = pd.Series(myTickerList.Tick)
#        myTicker =  col1[i]
#        myFilename = myTicker + "_bs" + ".csv"
#        myPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\Balance Sheets',myFilename)
#        bsData = yf.Ticker(myTicker).balancesheet
#        bsData.to_csv(myPath)
# =============================================================================
       
# =============================================================================
# for i in myTickerList.index:
#         # print(i)
#         col1 = pd.Series(myTickerList.Tick)
#         myTicker =  col1[i]
#         print(myTicker)
#         myPeriod = "240mo"
#         myInterval = "1d"
#         myFilename = myTicker + "_" + myPeriod + "_" + myInterval + ".csv"
#         myPath = os.path.join(r'C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\Stock Price History',myFilename)
#         priceData = yf.Ticker(myTicker).history(tickers=myTicker,period = myPeriod,interval = myInterval)
#         priceData.to_csv(myPath)
# =============================================================================

"""       
maintain watchlist which is the _ delimited first characters of each file in the stock price data directory
read in last date in each of those .csvs, and current date, and update each of those .csvs with the data b/w last and now
by reading into new dataframe, reading old into dataframe, and JOINing these, removing dupes
"""

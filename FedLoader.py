# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:11:03 2022

@author: Alex
"""

import pandas as pd
import os as os
import yfinance as yf

M1 = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\MacroEconomic\M1.csv")
FedFunds = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\MacroEconomic\FedFundsRate.csv")
M0 = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\MacroEconomic\M0.csv")
M2 = pd.read_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\MacroEconomic\M2.csv")

Comb = M1
#FedFunds = FedFunds[FedFunds.DATE.isin(M1.DATE)]
M1fed = pd.merge(M1, FedFunds, on='DATE', how='outer')
M1fed = pd.merge(M1fed, M2, on='DATE', how='outer')
#M1fed = pd.merge(M1fed, M0, on='DATE', how='outer')
#M1fed['DATE'] = pd.to_datetime(M1fed['DATE'])
#M1fed.sort_values(by='DATE')
M1fed.to_csv(r"C:\Users\Alex\Desktop\PROJECTS\Quant Trader\Data\MacroEconomic\M1-FedFnds.csv")
#M1['fedfund'] = FedFunds['DFF']
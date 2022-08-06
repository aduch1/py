# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#GENERAL LEARNING SYNTAX, STRINGS, PANDAS DATAFRAMES, ARRAYS(LISTS), PD.SERIES
import pandas as pd
import numpy as nm
import yfinance as yf
y =  pd.Series([1, 6, 8, 10])
a = ([1,2],[1,7])
z = ([1,2],[1,7])
print (y.size)
print(y)
#print(z.empty)
print("This line will be printed.")


print(nm.linalg.det(z))
print("This line will be printed.")
x = 1
if x == 1:
    # indented four spaces
    print("x is 1.")
    
myarr = [1,2,3,4,5,6,7,8,9] 
myarr2 = ["bruh"]

myarr[1] = 100
print(myarr[1:4])

myarr.append("nig")

print(myarr)

myarr.copy()

print(myarr)

myDF1 = pd.read_csv(r"C:\Users\Alex\Documents\book1.csv")
myDF2 = pd.read_csv(r"C:\Users\Alex\Documents\book2.csv")

#SET OPERATIONS
#SET UNION
union = pd.concat([myDF1,myDF2],ignore_index = True)
union = union.drop_duplicates()
print("UNION")
print(union)

#SET INTERSECTION
intersection = myDF1.merge(myDF2)
print("intersection")
print(intersection)

#SET DIFFERENCE
difference1 = myDF1[myDF1.Col1.isin(myDF2.Col1) == False]
difference2 = myDF2[myDF2.Col1.isin(myDF1.Col1) == False]
print("difference")
print(difference1)
print(difference2)

def unionF(df1,df2):
    joined = pd.concat([df1,df2],ignore_index = True)
    unionF = joined.drop_duplicates()    
    return unionF  

def intersectionF(df1,df2):
    intersectionF = df1.merge(df2)
    return intersectionF

def differenceF(df1,df2):
    differenceF = df1[df1.Col1.isin(df2.Col1) == False]
    return differenceF

print("union")
print(unionF(myDF1,myDF2))
test = unionF(myDF1,myDF2)
test['mvgAvg10d'] = test['Col3'].rolling(3,min_periods=3).mean()
print(test)






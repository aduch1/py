# -*- coding: utf-8 -*-
#setAlgebra
"""
Created on Tue Jul  5 07:38:52 2022

@author: Alex
"""
import pandas as pd
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
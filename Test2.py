# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 07:40:15 2022

@author: Alex
"""

import pandas as pd
import SetAlgebra as sa
#import plotly.io as px
import plotly.graph_objects as go
import plotly.express as px

myDF1 = pd.read_csv(r"C:\Users\Alex\Documents\book1.csv")
myDF2 = pd.read_csv(r"C:\Users\Alex\Documents\book2.csv")
myDF3 = pd.read_csv(r"C:\Users\Alex\Documents\book5.csv")






print("union")
print(sa.unionF(myDF1,myDF2))
print("intersection")
print(sa.intersectionF(myDF1,myDF2))
print("difference")
print(sa.differenceF(myDF1,myDF2))

fig1 = go.Figure(
    data=[go.Bar(y=[2,1,3])],
    #data=[go.Scatter(myDF3, x=myDF3.Item, y=myDF3.Qty)],
    layout_title_text="test"
)
fig1.show(renderer="browser", width=800, height=300)

fig2 =px.scatter(myDF3, x=myDF3.Item, y=myDF3.Qty)  
fig1.show(renderer="browser", width=800, height=300)
fig2.show(renderer="browser")
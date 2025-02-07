# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 15:27:02 2025

@author: vishal.yadav
"""


import pandas as pd
import os
import re

abs_file_name= os.path.join(os.getcwd(),'cap_rooms.csv')

def fix_denomination(amount):
    amount=amount.replace(',','')
    if isinstance(amount, (int,float)):
        return amount
    if isinstance(amount, str):
        matches = re.findall(r'\d+', amount)
        x= [float(match) for match in matches]
        if x:
            return x[0]
        else: return 0
    else: return 0


#1st--------------------------------------------------------------
df = pd.read_csv(abs_file_name)
df_sorted = df.sort_values(['PType', 'Reviews'], ascending=[True, False])
top_3_rooms = df_sorted.groupby('PType').head(3)


#2nd--------------------------------------------------------------------
df['PPN']= df['PPN'].apply(fix_denomination)
result = df.groupby('City')['PPN'].agg(cheapest='min', costliest= 'max')
print(result)

#3rd------------------------------------------------------------------------
import matplotlib.pyplot as plt
df['average PPN']=df.groupby('City')['PPN'].mean()
df.reindex()
df.plot(x='City',y='average PPN')


#4th--------------------------------------------------------------
correlation_PPN_beds = df['PPN'].corr(df['Beds'])
df.plot(x='PPN',y='Beds')


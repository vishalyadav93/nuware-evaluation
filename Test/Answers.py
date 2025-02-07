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
top_3_rooms.to_csv('Answer1.csv')
print(top_3_rooms)

#2nd--------------------------------------------------------------------
df['PPN']= df['PPN'].apply(fix_denomination)
result = df.groupby('City')['PPN'].agg(cheapest='min', costliest= 'max')
result.to_csv('Answer2.csv')
print(result)

#3rd------------------------------------------------------------------------
df['average PPN'] = df.groupby('City')['PPN'].transform('mean')
df.plot(x='City', y='average PPN', kind='bar', figsize=(10, 6)) #Kind = 'bar' for bar plot


#4th--------------------------------------------------------------
correlation_PPN_beds = df['PPN'].corr(df['Beds'])
df.plot(x='PPN',y='Beds')


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:02:54 2020

@author: tejaspatel
"""


import pandas as pd

#poblem 3a

df = pd.DataFrame({'days':[1,1,2,2,1,3,4],'values':[10,10,5,3,-2,4,20]})

combined = df.groupby('days').agg({'values': ['mean', 'median', 'max','min']})

combined.columns = ['mean_values','median_values','max_values','min_values']


print(combined) #final dataframe of problem 3a


#problem 3b

df1 = pd.DataFrame({'employee': [1001, 1002, 1004, 1001, 1001, 1002, 1004, 1005, 1005],
                       'pos': [2, 2, 2, 2, 2, 2, 2, 2, 2],
                       'amount': [125, 542, 2345, 892, 100, 1234, 657, 34, 35]})


df2 = df1.groupby(['employee','pos'])['amount'].agg(['max','min'])

df2['diff'] = df2['max']-df2['min']

df3 = df2.sort_values(['diff'],ascending=False).head(2)

df4 = df3[['diff']]
print(df4)          #final dataframe of problem 3b
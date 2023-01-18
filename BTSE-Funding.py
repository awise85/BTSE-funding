#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 22:49:16 2022

@author: adamwise
"""

import requests 
import pandas as pd
from IPython.display import display

#import numpy as np
import os
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates

#import datetime

print("Input Symbol")
symbol = input()+"PFC"

btsefunding = requests.get('https://api.btse.com/futures/api/v2.1/funding_history', params={'symbol': symbol}).json()[symbol]

# json into pandas
df = pd.DataFrame(btsefunding)

# format df
df['time'] = (pd.to_datetime (df['time'], unit='s'))
df.drop('symbol', axis=1, inplace=True)
df['rate annualised'] = df['rate'] * 24 * 365
pd.options.display.float_format = '{:,.4%}'.format

#df.style.format({'time': "{:.2f}",'rate': "{:.3f}"})

df.style


# print df & info
display(df)
print(df.info())




# draw chart
plt.plot(df['time'], df['rate'])

plt.xlabel('time')
plt.ylabel('rate')

plt.axhline(y = 0, color = 'black', linestyle =':')
plt.title(symbol + ' funding')



plt.show()

# export to CSV
file_dir = os.path.dirname(os.path.abspath(__file__))
file_folder = 'csv files'
file_name = 'BTSE-Funding.csv'
file_path = os.path.join(file_dir, file_folder, file_name)
df.to_csv(file_path, header = True, index = True)



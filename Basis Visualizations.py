# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:23:34 2025

@author: gabea
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:/Users/gabea/OneDrive/Documents/Spring 25/Trading/Homework Assignment #1.xlsx", sheet_name="HSC")
df['Date'] = pd.to_datetime(df['Date'])

JanMar = df[['Jan', 'Feb', 'Mar']]
AprJun = df[['Apr', 'May', 'Jun']]
JulSep = df[['Jul', 'Aug', 'Sep']]
OctDec = df[['Oct', 'Nov', 'Dec']]

# Create a grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.5)


# Plot Jan-Mar
for col in JanMar:
    axes[0, 0].plot(df['Date'], JanMar[col], label=col)
axes[0, 0].set_title("Jan-Mar")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Basis")
axes[0, 0].legend()
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot Apr-Jun
for col in AprJun:
    axes[0, 1].plot(df['Date'], AprJun[col], label=col)
axes[0, 1].set_title("Apr-Jun")
axes[0, 1].set_xlabel("Date")
axes[0, 1].set_ylabel("Basis")
axes[0, 1].legend()
axes[0, 1].tick_params(axis='x', rotation=45)

# Plot Jul-Sep
for col in JulSep:
    axes[1, 0].plot(df['Date'], JulSep[col], label=col)
axes[1, 0].set_title("Jul-Sep")
axes[1, 0].set_xlabel("Date")
axes[1, 0].set_ylabel("Basis")
axes[1, 0].legend()
axes[1, 0].tick_params(axis='x', rotation=45)


# Plot Oct-Dec
for col in OctDec:
    axes[1, 1].plot(df['Date'], OctDec[col], label=col)
axes[1, 1].set_title("Oct-Dec")
axes[1, 1].set_xlabel("Date")
axes[1, 1].set_ylabel("Basis")
axes[1, 1].legend()
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

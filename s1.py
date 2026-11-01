import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Bestsellers with categories (1).csv")

data.head(5)
data.info()
data.isnull().sum()
data['User Rating'].unique()

df = np.mean(data['User Rating'])

print(df)

df = np.median(data['User Rating'])

print(df)

df = data['User Rating'].mode()[0]

print(df)


data['Price'].unique()

df2 = np.mean(data['Price'])

print(df2)

df2 = np.median(data['Price'])

print(df2)

df2 = data['Price'].mode()[0]

print(df2)


data['Reviews'].unique()

df3 = np.mean(data['Reviews'])

print(df3)

df3 = np.median(data['Reviews'])

print(df3)

df3 = data['Reviews'].mode()[0]

print(df3)
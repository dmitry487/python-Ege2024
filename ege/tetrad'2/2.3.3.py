import pandas as pd
url = 'https://raw.githubusercontent.com/akmand/datasets/main/diamonds.csv'
d = pd.read_csv(url)
print(d.head (2))
print(" ")
print(d.tail(3))
print(" ")
print(d.shape)
print(" ")
print(d.describe())
print(" ")
print(d.iloc[6:9])
print(" ")
print(d[d['quanter']=='3'].head())
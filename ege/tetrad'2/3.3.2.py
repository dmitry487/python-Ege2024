import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler1 = MinMaxScaler()
scaler2 = StandardScaler ()
d=pd.read_csv('https://raw.githubusercontent.com/akmand/datasets/master/iris.csv')
d['sepal_length_cm']= scaler1.fit_transform(d[['sepal_length_cm']])
d['sepal_width_cm']= scaler2.fit_transform(d[['sepal_width_cm']])
print(d.head ())
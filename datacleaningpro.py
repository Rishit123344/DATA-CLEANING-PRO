import csv
import pandas as pd 
df = pd.read_csv("brightstars.csv")
print(df.shape)
del df['lum']
print(df.shape)
df = df.rename({
    'lum':'luminosity'
},axis = 'columns')
df.to_csv('mainpro_csv')



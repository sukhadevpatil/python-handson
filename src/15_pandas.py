
import pandas as pd

df = pd.read_csv('my_csv.csv')

print(df.head(4))        #this will print first 4 rows of data
print('===================================')

print(df.info())         #will print concise summary of DataFrame's structure

print('===================================')
print(df.describe())     # statistical summary of the numerical columns

print('===================================')

df['Total'] = df['Order_Quantity'] * df['Order_Price']

print(df.head(4))

df.to_csv('updated_my_csv.csv', index=False)
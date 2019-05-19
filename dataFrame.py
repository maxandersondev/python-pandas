import pandas as pd

df = pd.read_csv('data/gapminder.tsv', sep='\t')

print(type(df))  #get data type

print(df.shape)  #get datafram shape - length and width

print(df.columns)  #get headers of data

print(df.dtypes)   #get column data types

print(df.info())   #more info on the data

print(df.head())   #get top 5 rows of data


#subsetting columns

country_df = df['country']  #just get the country column
print(country_df.head())
print(country_df.tail())

subset = df[['country', 'continent', 'year']]
print(subset.head())

#get subsets of row indexes

print(df.loc[0])  #get first row

print(df.loc[100:200])  #get a slice of data using the python slicing functionality

print(df.loc[[0,99,999]])

#get the last row
number_of_rows = df.shape[0]

print(df.loc[number_of_rows-1])

#iloc is just like loc, but deals with indexes like -1
#print(df.loc[-1])  #won't work
print(df.iloc[-1])  #will work getting last row

#having fun with slicing and column selection
print(df.loc[99:999, ['year', 'pop']])

print(df.iloc[:, [2,4,-1]])


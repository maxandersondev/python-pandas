import pandas as pd
import matplotlib.pyplot as plt

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

#playing with ranges

small_range = list(range(5))
print(small_range)

print(df.iloc[:, small_range])
print(df.iloc[:, :5])  # better way to do what I did just above

print(df.iloc[:, 0:6:])
print(df.iloc[:, 0::2])  #start:end:step
print(df.iloc[100:200:5, 0::2])

print(df.iloc[[0,99,999], [0, 3, 5]])
print(df.iloc[[0,99,999], 0::2])

print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])  # still can use row indexes with loc

#data aggrigations


print(df.groupby('year')['lifeExp'].mean())

#multiple column groupings
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

flat = multi_group_var.reset_index()
print(flat)

print(df.groupby('continent')['country'].nunique())

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

#had to add backend to ~/.matplotlib/matplotlibrc
# Backend:  MacOSX
global_yearly_life_expectancy.plot()
plt.show()




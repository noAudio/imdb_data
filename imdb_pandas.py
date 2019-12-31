# pandas is the library used to read the file
import matplotlib.pyplot as plt
import pandas as pd

# assign the excel file to a variable
# then use the pandas function 'read_excel'
# to read the data in the file into a dataframe
excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)

# use variable.head() to display the first
# few rows of the data
print(movies.head())

# read the first sheet and set Title column
# as the index
movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
print(movies_sheet1.head())

# read the second and third sheets
movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
print(movies_sheet2.head())
movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)

# since the data in the sheets is similar we
# will combine dataframes and overwrite the
# original one then use shape to check the data
movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])
print(movies.shape)

# alternatively use ExcelFile when working with
# a document that has several sheets to increase
# performance
# xlsx = pd.ExcelFile(excel_file) #parse the doc using ExcelFile
# movies_sheets = [] # create an array to hold the data
# for sheet in xlsx.sheet_names: # a loop to iterate through the sheets and create dataframes
# movies_sheets.append(xlsx.parse(sheet))
# movies = pd.concat(movies_sheets) # combine the dataframes into one

# check the 5 bottom rows using tail()
print(movies.tail())

# use sort_values to sort the sheet based
# on the Gross Earnings column
sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)

# display top ten movies by Gross Earnings
sorted_by_gross["Gross Earnings"].head(10)

# import pyplot from matplotlib to visualize
# the data
# plt.show(sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh"))

# plost a histogram to visualize the distribution
# plt.show(movies['IMDB Score'].plot(kind='hist'))

# use pandas describe() to get statistical
# analysis of the numeric data in the frame
print(movies.describe())

# create a new column where Net Earnings are
# calculated by subtracting Budget from Gross
# Earnings
movies['Net Earnings'] = movies['Gross Earnings'] - movies['Budget']

# sort movies by Net Earnings
sorted_movies = movies[['Net Earnings']].sort_values(
    ['Net Earnings'], ascending=[False])
plt.show(sorted_movies.head(10)['Net Earnings'].plot.barh())

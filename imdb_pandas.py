# pandas is the library used to read the file
import pandas as pd

# assign the excel file to a variable
# then use the pandas function 'read_excel'
# to read the data in the file into a dataframe
excel_file = 'movies.xls'
movies = pd.read_excel(excel_file)

# use variable.head() to display the first
# few rows of the data
print(movies.head())

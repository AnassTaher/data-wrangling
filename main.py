# import athelete_events.csv file
# import pandas as pd

import pandas as pd
import numpy as np

pd = pd.read_csv('athlete_events.csv')

# print the first 5 rows of the dataframe
print(pd.head())
# print the column names
print(pd.columns)

columns_to_be_cleaned = ['Age', 'Team', 'Medal']
# remove the rows with missing values in the columns
pd = pd.dropna(axis=0, subset=columns_to_be_cleaned)

# check for any null values
print(pd.isnull().sum())


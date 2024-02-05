# import athelete_events.csv file
# import pandas as pd

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd = pd.read_csv('athlete_events.csv')

# print the first 5 rows of the dataframe
# print(pd.head())
# print the column names
# print(pd.columns)

columns_to_be_cleaned = ['Age', 'Team']
# remove the rows with missing values in the columns
pd = pd.dropna(axis=0, subset=columns_to_be_cleaned)

print(pd.shape)
# ID Name Sex Age Height Weight Team NOC Games Year Season City Sport Event Medal
# check for any null values

#  get the minimum and maximum age of the atheletes
min_age = pd['Age'].min()
max_age = pd['Age'].max()

# Under 18 18-24 25-34 35-44 45-54 55-64 65 and over

age_groups = [
  (0, 18),
  (18, 24),
  (25, 34),
  (35, 44),
  (45, 54),
  (55, 64),
  (65, 100)
]

# create a graph of the age groups, x axis is the age group, y axis is the number of atheletes

# create a new column called age_group
pd['Age Group'] = pd['Age'].apply(lambda x: 'Under 18' if x < 18 else '18-24' if x < 24 else '25-34' if x < 34 else '35-44' if x < 44 else '45-54' if x < 54 else '55-64' if x < 64 else '65 and over')


# print the different values that are possible for 'Medal'
print(pd.head())

# print null values
print(pd.isnull().sum())
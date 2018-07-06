# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:02:29 2018

@author: Jijumn
"""

#Data preprocessing template

import numpy as np
import pandas as pd

#reading the data

NFL_Dataset = pd.read_csv("NFL Play by Play 2009-2017 (v4).csv")


#set seed

np.random.seed(0)

#to look at few rows of the data

NFL_Dataset.sample(5)


#to check how many missing data is there

missing_values_count = NFL_Dataset.isnull().sum()

#missing values in first 10 columns

missing_values_count[0:10]

#how many total missing values do we have

total_cells = np.product(NFL_Dataset.shape)
total_missing = missing_values_count.sum()

#%of data missing
(total_missing/total_cells)*100

#Number of missing points in the first 10 columns

missing_values_count[0:10]

#Look at the # of missing points in the sorted series

missing_values_count.sort_values(ascending=False)[10:20]

#One way is to drop the rows having missing values 
NFL_Dataset.dropna()

#Column wise removal of columns with atleast one missing value

columns_with_na_dropped = NFL_Dataset.dropna(axis=1)
columns_with_na_dropped.head()


#to check how much data did we loose

print("columns in original dataset: %d" % NFL_Dataset.shape[1])
print("columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

#2nd method to fill the missing values


#to get a small subset of the NFL dataset

subset_nfl_data = NFL_Dataset.loc[:, 'EPA':'Season'].head() 

subset_nfl_data

#to fill the NAN value with 0

subset_nfl_data.fillna(0)

#to fill the subset null value with the susequent values and then replace all the remaining na's with 0

subset_nfl_data.fillna(method = 'bfill', axis=0).fillna(0)




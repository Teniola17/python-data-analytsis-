import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

# import a dataset from a CSV file
df = pd.read_csv("https://rcs.bu.edu/examples/python/DataAnalysis/flights.csv")

print(df.head())

print(df.info())

print(df.isnull().sum())

print("missing percentAGE:", df.isnull().mean()*100)

print(df.shape)

# duplicates
print(df.duplicated().sum())

# drop duplicates
df = df.drop_duplicates() # this will drop the duplicate rows from the dataframe

#df = df.dropna() # this will drop the rows with missing values from the dataframe


# impute the missing observations with the mean value of the column
imputer = SimpleImputer(strategy='mean') # this will create an imputer object with the strategy of mean
num_cols = df.select_dtypes(include=['float64', 'int64']).columns # this will select the numerical columns from the dataframe
df[num_cols] = imputer.fit_transform(df[num_cols]) # this will fit the imputer object to the numerical columns and transform the missing values with the mean value of the column


# impute categotial variables with the most frequent value
imputer_cat = SimpleImputer(strategy='most_frequent') # this will create an imputer object with the strategy of most frequent
cat_cols = df.select_dtypes(include=['object']).columns # this will select the categorical columns from the dataframe
df[cat_cols] = imputer_cat.fit_transform(df[cat_cols]) # this will fit the imputer object to the categorical columns and transform the missing values with the most frequent value of the column



print(df.info()) # to check the info of the dataframe after dropping duplicates and missing values

print(df.isnull().sum()) # to check the number of missing values in each column after dropping duplicates and missing values
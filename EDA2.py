import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# create a sample dataframe
data = {
    "name": ["John", "Tola", "Sara", "Mike", "Anna"],
    "age": [30, 25, 28, 35, 22],
    "city": ["New York", "London", "Tokyo", "Chicago", "Paris"],
    "height": [1.75, 1.65, 1.80, 1.70, 1.60],
}

print(data)

df1 = pd.DataFrame(data)
print(df1)

# import a dataset from a CSV file
df2 = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/freshman_kgs.csv')

print(df2.head())

# inspect the DATASET

print(df2.columns) # this will print the column names of the dataframe


print(df2.info()) # this will print the summary of the dataframe including the number of non-null values and the data types of each column


print(df2.describe())   # this will print the summary statistics of the numerical columns in the dataframe

print(df2.shape) # this will print the number of rows and columns in the dataframe

print(df2.isnull().sum()) # this will print the number of missing values in each column of the dataframe

print(df2['Sex'].value_counts()) # this will print the count of each unique value in the 'Sex' column

# make the variable names more readable
df2.columns = (
    df2.columns
      .str.replace('"', '', regex=False) # this will remove the double quotes from the column names
      .str.strip() # this will remove any leading or trailing whitespace from the column names
      .str.replace(' ', '_') # this will replace any spaces in the column names with underscores
      .str.replace('[()]', '', regex=True) # this will remove any parentheses from the column names
)

print(df2.columns)

## univariate analysis

print(df2['Weight_Apr'].groupby(df2['Sex']).mean())# this will create a histogram of the 'Weight_Apr' column grouped by 'Sex'

# for BMI in April
print(df2['BMI_Apr'].groupby(df2['Sex']).mean()) # this will create a histogram of the 'BMI_Apr' column

# plot histogram for BMI in April

plt.figure() # this will create a new figure for the plot
sns.histplot(df2['BMI_Apr'], kde=True) # this will create a histogram of the 'BMI_Apr' column with a kernel density estimate (KDE) curve
plt.title("Distribution of BMI of Freshmen in April") # this will set the title of the plot
plt.xlabel("BMI in April (kg/m^2)")    # this will set the label for the x-axis


# plot the boxplot of BMI in April
sns.boxplot(y=df2["BMI_Apr"]) # this will create a boxplot of the 'BMI_Apr' column
plt.title("Boxplot of BMI of Freshmen in April") # this will set the title of the plot
plt.ylabel("BMI in April (kg/m^2)") # this will set the label for the y-axis
plt.show() # this will display the plot



### statistical tests
from scipy.stats import ttest_ind
male_BMI = df2[df2['Sex'] == 'M']['BMI_Apr']
female_BMI = df2[df2['Sex'] == 'F']['BMI_Apr']
t_stat, p_value = ttest_ind(male_BMI, female_BMI)
print(f"T-statistic: {t_stat}, P-value: {p_value}") 

from scipy.stats import ttest_ind
male_w = df2[df2['Sex'] == 'M']['Weight_Apr']
female_w = df2[df2['Sex'] == 'F']['Weight_Apr']
t_stat, p_value = ttest_ind(male_w, female_w)
print(f"T-statistic: {t_stat}, P-value: {p_value}") 

#### using a paired t-test to compare the weights of the same students in April and September
from scipy.stats import ttest_rel
april_weights = df2['Weight_Apr']
september_weights = df2['Weight_Sep']
t_stat, p_value = ttest_rel(april_weights, september_weights)
print("Paired T-test results:")
print(f"T-statistic: {t_stat}, P-value: {p_value}")


# for BMI in April and September
april_BMI = df2['BMI_Apr']
september_BMI = df2['BMI_Sep']
t_stat, p_value = ttest_rel(april_BMI, september_BMI)
print("Paired T-test results for BMI:")
print(f"T-statistic: {t_stat}, P-value: {p_value}")

############## correlation analysis
correlation_matrix = df2[['Weight_Apr', 'Weight_Sep', 'BMI_Apr', 'BMI_Sep']].corr()
print(correlation_matrix)

# plot the correlation matrix using a heatmap
plt.figure(figsize=(8, 6)) # this will set the size of the figure
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5) # this will create a heatmap of the correlation matrix with annotations and a color map
plt.title("Correlation Matrix of Weights and BMI in April and September") # this will set the title of the plot
plt.show() # this will display the plot


# pairplot to visualize the relationships between the variables
sns.pairplot(df2[['Weight_Apr', 'Weight_Sep', 'BMI_Apr', 'BMI_Sep']]) # this will create a pairplot of the specified columns
plt.suptitle("Pairplot of Weights and BMI in April and September", y=1.02) # this will set the title of the plot
plt.show() # this will display the plot

# boxplot by sex of bmi in april
sns.boxplot(x=df2["Sex"], y=df2['BMI_Apr']) # this will create a boxplot of the 'BMI_Apr' column grouped by 'Sex
plt.title("Boxplot of BMI of Freshmen in April by Sex") # this will set the title of the plot
plt.xlabel("Sex") # this will set the label for the x-axis
plt.ylabel("BMI in April (kg/m^2)") # this will set the label for the y-axis
plt.show() # this will display the plot

# april weights by sex
sns.boxplot(x=df2["Sex"], y=df2['Weight_Apr']) # this will create a boxplot of the 'Weight_Apr' column grouped by
plt.title("Boxplot of Weights of Freshmen in April by   Sex") # this will set the title of the plot
plt.xlabel("Sex") # this will set the label for the x-axis
plt.ylabel("Weight in April (kg)") # this will set the label for the y-axis
plt.show() # this will display the plot

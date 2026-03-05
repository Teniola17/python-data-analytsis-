import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# create a sample dataframe
data = {
    "name": ["John", "Tola", "Sara", "Mike", "Anna"],
    "age": [30, 25, 28, 35, 22],
    "city": ["New York", "London", "Tokyo", "Chicago", "Paris"],
    "height": [1.75, 1.65, 1.80, 1.70, 1.60],
}

df = pd.DataFrame(data)

# display the first few rows of the dataframe
print(df.head())
# summary statistics of the dataframe
print(df.describe())

# load a dataset from a CSV file
df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/freshman_kgs.csv')

print(df.head())
df.columns = (
    df.columns
      .str.replace('"', '', regex=False)
      .str.strip()
      .str.replace(' ', '_')
      .str.replace('[()]', '', regex=True)
)

print(df.columns)

# filter for only the male students
male_students = df[df['Sex'] == 'M']['Weight_Apr']

plt.ion
plt.figure() 
sns.histplot(male_students, kde=True)
plt.title("Distribution of Weights of Male Freshmen in April")
plt.xlabel("Weight (kg)")   
  

plt.figure() 

sns.boxplot(x=df["Sex"],y=df['Weight_Apr'])
plt.title("Boxplot of Weights of Freshmen in April by Sex")
plt.xlabel("Sex")
plt.ylabel("Weight (kg)")       
plt.show()

### statistical tests
from scipy.stats import ttest_ind
male_weights = df[df['Sex'] == 'M']['Weight_Apr']
female_weights = df[df['Sex'] == 'F']['Weight_Apr']
t_stat, p_value = ttest_ind(male_weights, female_weights)
print(f"T-statistic: {t_stat}, P-value: {p_value}")
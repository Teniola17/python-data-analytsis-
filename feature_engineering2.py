import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.linear_model import LogisticRegression
#from sklearn.impute import SimpleImputer

#df_local = pd.read_csv("C:\\Users\\EmmanuelAdewuyi\\OneDrive - London School of Hygiene and Tropical Medicine\\Documents\\Frequencies.csv")

# import a dataset from a CSV file
df = pd.read_csv("https://raw.githubusercontent.com/jeffheaton/aifh/master/vol1/python-examples/datasets/breast-cancer-wisconsin.csv")
print(df.head())

#inspect the dataset
print(df.columns) # this will print the column names of the dataframe
print(df.info()) # this will print the summary of the dataframe including the number of non-null values and the data types of each column
print(df.describe())   # this will print the summary statistics of the numerical columns in the dataframe
print(df.shape) # this will print the number of rows and columns in the dataframe
print(df.isnull().sum()) # this will print the number of missing values in each column of the dataframe
print(df['class'].value_counts()) # this will print the count of each unique value

# convert the target variable to categorical

label_encoder = LabelEncoder() # this will create a label encoder object
df['class'] = label_encoder.fit_transform(df['class']) # this will fit the label encoder object to the 'class' column and transform the values to numerical values
print(df['class'].value_counts()) # this will print the count of each unique value in the 'class' column after encoding

# examine each feature and its relationship with the target variable
#for column in df.columns[1:-1]: # this will loop through all the columns except the last one (target variable)
 #   plt.figure() # this will create a new figure for the plot
 #   sns.boxplot(x=df['class'], y=df[column]) # this will create a boxplot of the column grouped by the target variable
 #   plt.title(f"Boxplot of {column} by class") # this will set the title of the plot
 #   plt.xlabel("Class") # this will set the x-axis label
#    plt.ylabel(column) # this will set the y-axis label
  #  plt.show() # this will display the plot

# plot scatter plot for epitelia size and clum thickness clolored by class
plt.figure()
sns.scatterplot(x=df['bland_chromatin'], y=df['clump_thickness'], hue=df['class']) # this will create a scatter plot of 'epithelial_size' and 'clump_thickness' colored by the target variable
plt.title("Scatter plot of epithelial size and clump thickness colored by class") # this will set the title of the plot
plt.xlabel("Epithelial Size") # this will set the x-axis label  
plt.ylabel("Clump Thickness") # this will set the y-axis label
plt.show() # this will display the plot

# logistic regression
X = df.drop(columns=['id', 'class']) # this will drop the 'id' and 'class' columns from the dataframe and assign the remaining columns to x
y = df['class'] # this will assign the 'class' column to y

print(X.info())
print(df['bare_nucleoli'].unique()) # this will print the unique values in the 'bare_nucleoli' column
X['bare_nucleoli'] = pd.to_numeric(X['bare_nucleoli'], errors='coerce') # this will convert the 'bare_nucleoli' column to numeric values, coercing any non-numeric values to NaN

print(X['bare_nucleoli'].info()) # this will print the summary of the dataframe after converting the 'bare_n
X = X.dropna() # this will drop the rows with missing values from the dataframe
y = y[X.index] # this will select the corresponding values from the target variable for the
#print(X['bare_nucleoli'].isnull().sum()) # this will print the number of missing values in each column of the dataframe after converting the 'bare_nucleoli' column to numeric values
model = LogisticRegression() # this will create a logistic regression model object
model.fit(X, y) # this will fit the logistic regression model to the data   
#call for the coefficients of the model
print(model.coef_) # this will print the coefficients of the logistic regression model

print(model.predict_proba(X)) #this will return the predicted probabilities for each class for the input data X

print(model.predict_proba(X)[:, 1] )# this will return the predicted probabilities for the positive class (class 1) for the input data X
df = df.loc[X.index]
df['predicted_probabilities'] = model.predict_proba(X)[:, 1] # this will add a new column to the dataframe with the predicted probabilities for the positive class
print(df.head()) # this will print the first few rows of the dataframe with the new column

plt.figure() # this will create a new figure for the plot
sns.scatterplot(x=df['predicted_probabilities'], y=df['clump_thickness'], hue=df['class']) # this will create a scatter plot of the predicted probabilities and 'clump_thickness' colored by the target variable
plt.axvline(x=0.5, color='red', linestyle='--') # this will add a vertical line at x=0.5 to indicate the threshold for classification
plt.title("Scatter plot of predicted probabilities and clump thickness colored by class") # this will set the title of the plot
plt.xlabel("Predicted Probabilities") # this will set the x-axis label  
plt.show() # this will display the plot


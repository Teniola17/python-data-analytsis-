for i in range(50):
    print("Iran is the best country in the world")
    

#  print the first nth elements of a fibonacci sequence

# n_i= n_{i-2} + n_{i-1}

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

n = 10

a = 1
b = 1
fibo = []
for i in range(n):
    fibo.append(a)
    a,b = b, a+b

print(fibo)

counts = 1
while counts<=8:
    print(counts)
    counts+=1
    
    
    
    
############################################################

import math # very important to import math module to use math functions

print('the sin of 90: ',math.sin(math.radians(90)))

print('the square root of 16: ',math.sqrt(16))

######    variable types
age = 45 # age is an integer variable
print(type(age))

name = "John" # name is a string variable
print('the type of name is',type(name))

height = 1.75 # height is a float variable
print('the type of height is',type(height))

True # this is a boolean value
50 < 45 # this is a boolean expression that evaluates to False


######### Operators on strings
first_name = "John"
last_name = "Harry"
full_name = first_name + " " + last_name # string concatenation
print(full_name)

print(first_name*3) # string repetition
print(len(full_name)) # length of the string
print(full_name.capitalize()) # capitalize the first letter of the string
print(full_name.upper()) # convert the string to uppercase
print(full_name.lower()) # convert the string to lowercase  


######### boolean operators
Age = 5

if Age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")    
    

###### List
my_list = [1, 2, 3, 4, 5] # this is a list of integers   
my_list2 = [2, "apple", 3.14, True] # this is a list of mixed data types
print(my_list2)

# append the two lists together
combined_list = my_list + my_list2
print(combined_list)
my_list2.append(6) # this will add 6 to the end of my_list2
print(my_list2)
## reference/ accessing elements in a list
print(my_list[0]) # this will print the first element of my_list which is
# remove the last element of my_list2
my_list2.remove(6)
# modify the first element of my_list
my_list[0] = 10
print(my_list)


######################### dictionary
my_dict = {
    "name": "John", 
    "age": 30, 
    "city": "New York",
    "height": 1.75,
    } # this is a dictionary with string keys and values of different types
print(my_dict)

my_dict2 = {
    "name": ["John", "Tola", "Sara"],
    "age": [30, 25, 28],
    "city": ["New York", "London", "Tokyo"],
    "height": [1.75, 1.65, 1.80],
    } 

my_dict2["city"][1] = "Chicago" # this will change the second element of the list associated with the key "city" to "Chicago"

print(my_dict2)

print(my_dict2["name"]) # this will print the value associated with the key "name"

print(my_dict2["city"])

############### creating a virtual environment
# 1. open terminal and navigate to the project directory
# 2. create a virtual environment using the command: python -m venv venv
# 3. activate the virtual environment using the command: source venv/bin/activate (for macOS/Linux) or venv\Scripts\activate (for Windows)
# 4 ctrl + shift + p and select "Python: Select Interpreter" and choose the interpreter from the virtual environment (venv)
# 5. install the required packages using the command: pip install -r requirements.txt

# pip install numpy pandas matplotlib seaborn scikit-learn

import numpy as np
import pandas as pd

df1 = pd.DataFrame(my_dict2)

print(df1)

df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv')
print(df.head(5))


import numpy as np  # Library to work with numerical data in Python
                    # Provides an object called n-dimensional array
import pandas as pd # Series: 1D ndarray, DataFrame: 2D ndarray
import matplotlib.pyplot as plt  # Library for creating static, animated, and interactive visualizations
from sklearn.model_selection import train_test_split

# Creating a 2D array
a = np.array([[1,3,4],[4,5,6]])
print(a[1])  # Prints the second row of the array `a`

# Creating another 2D array
b = np.array([[12,23,34],[13,14,15]])

# Concatenating two arrays along different axes
c = np.concatenate((a,b)) # Concatenates `a` and `b` along the first axis (rows), resulting in a 4x3 matrix
d = np.concatenate((a,b), axis=1) # Concatenates `a` and `b` along the second axis (columns), resulting in a 2x6 matrix
print(c)
print(d)

# Creating and sorting a 1D array
e = np.array([2,3,5,1,6])
f = np.sort(e) # Sorts the array `e`
print(f)
print(e.size) # Returns the number of elements in the array `e`
print(c.shape) # Returns the dimensions of the array `c`
print(e.ndim)  # Returns the number of dimensions of the array `e`

# Broadcasting example:
print("############")
g = np.array([[1,2,3],[4,5,6]]) # 2D array
h = np.array([10,20,30])        # 1D array
i = g + h  # Adds `h` to each row of `g` (broadcasting)
print(i)
j = g * h  # Multiplies `h` with each row of `g` (broadcasting)
print(j)

# Creating a pandas Series
cars = pd.Series(["BMW", 'Nissan', "Kia"])  
print(cars)

# Creating a pandas DataFrame from a dictionary
fam = {
    "1stborn": {
        "name": "Swati",
        "year": 1999
    },
    "2ndborn": {
        "name": "Shruti",
        "year": 2002
    }
}
family = pd.DataFrame(fam)
print(family)

# Importing data from a CSV file into a pandas DataFrame
df = pd.read_csv("annual-enterprise-survey-2021-financial-year-provisional-csv.csv")
print(df)
print("#########")
print(df.describe())  # Generates descriptive statistics of the DataFrame
print("#########")
print(df.info())  # Prints information about the DataFrame
print("#########")
print(df.head(6))  # Shows the first 6 rows of the DataFrame
print("#########")
print(df.tail(2))  # Shows the last 2 rows of the DataFrame
print("#########")
print(df.loc[3])  # Indexing: shows the 4th row (0-indexed) of the DataFrame
print("#########")
df.hist()  # Generates a histogram for each numeric column in the DataFrame
plt.show()  # Displays the histograms

k=[1,2,3,4]
l=[2,3,5,7]
# plt.plot(k,l)# plots the graph
# plt.show()# displays the graph

#different approach
fig = plt.figure()
m=fig.add_axes([0,0,1,1])
# m.plot(k,l)
# plt.show()
print("#########")
# Selecting the 'Year' column
n = df[['Year']]

# Dropping the 'Year' column
o = df.drop('Year', axis=1)#This line of code removes the 'Year' column from the DataFrame df. The resulting DataFrame o contains all the original columns except 'Year'.

# Splitting the data into training and testing sets
o_train, o_test, n_train, n_test = train_test_split(o, n, test_size=0.25)

print("Training data (o_train):")
print(o_train)
print("Testing data (o_test):")
print(o_test)
print("Training labels (n_train):")
print(n_train)
print("Testing labels (n_test):")
print(n_test)
# Pandas Series: it is like a column in a table. A one-dimensional array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. A Series is like a fixed-size dict in that you can get and set values by index label. It can also be thought of as a single column of a DataFrame.
import pandas as pd

#  Series from a list
countries = ['USA', 'Canada', 'Germany', 'UK', 'France']
series_countries = pd.Series(countries)

print("="*50)
print(series_countries)
print("="*50)

#  custom index

marks = [90, 80, 70, 60, 50]
subjects = ['Math', 'Science', 'English', 'History', 'Geography'] 
series_marks = pd.Series(marks, index=subjects, name='Marks')

print(series_marks)
print("="*50)

# series from a dictionary

marks_dict = {'Math': 90, 'Science': 80, 'English': 70, 'History': 60, 'Geography': 50}
series_marks_dict = pd.Series(marks_dict, name='Marks')

print(series_marks_dict)
print("="*50)

#  series attributes

print("size:", series_marks.size)  # Number of elements
print("name:", series_marks.name)  # Name of the Series
print("is_unique:", series_marks.is_unique) # Whether all elements are unique
print("shape:", series_marks.shape) # Dimensions of the Series
print("index:", series_marks.index)  # Index labels of the Series
print("values:", series_marks.values)  # Values of the Series

print("="*50)

# Series from read_csv
subs = pd.read_csv('Python/subs.csv').squeeze()  # squeeze() converts DataFrame to Series if possible
print(subs)
print(type(subs))  # Check the type of the 
print("="*50)

kruns = pd.read_csv('Python/kohli_ipl.csv', index_col=0).squeeze()  # squeeze() converts DataFrame to Series if possible
print(kruns)
print(type(kruns))  # Check the type of the 
print("="*50)

blw = pd.read_csv('Python/bollywood.csv', index_col='movie').squeeze()  # squeeze() converts DataFrame to Series if possible
print(blw)
print(type(blw))  # Check the type of the 
print("="*50)

#  Series methods

print("head():\n", subs.head(3))  # First n elements
print()
print("tail():\n", kruns.tail(3))  # Last n elements
print()
print("sample():\n", blw.sample(3))  # Random sample of n elements
print()
print("value_counts():\n", blw.value_counts())  # Count of unique values
print()
print("sort_values():\n", kruns.sort_values(ascending=False))  # Sort values in ascending or descending order
print()
print("sort_index():\n", blw.sort_index())  # Sort by index
print()
print("describe():\n", kruns.describe())  # Summary statistics
print("="*50)
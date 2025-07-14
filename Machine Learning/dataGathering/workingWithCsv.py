import pandas as pd 

# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv')
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv', sep=',') # Use sep=';' if the CSV is semicolon-separated
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv',  names=['col1', 'col2', 'col3','col4', 'col5', 'col6','col7', 'col8', 'col9','col10', 'col11']) # Use sep=';' if the CSV is semicolon-separated
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv', index_col=0) # convert the first column to index
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv',header= 0) # Use header=0 if the first row is the header
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv', usecols=[0, 1, 2]) # Use usecols to select specific columns
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv', skiprows=[2]) # Skip the first row
# df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv',encoding='utf-8') # Specify the encoding if needed
df = pd.read_csv('C:/Users/AlfejMansuriMAQSoftw/Downloads/untitled (3).csv', on_bad_lines='skip') # Skip bad lines
print(df.head())

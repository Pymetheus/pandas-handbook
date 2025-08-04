# --- Pandas Handbook: 01 - Data Structures ---


# --- Import Libraries ---
# Import the pandas library and alias it as pd
import pandas as pd


# --- Index Types in Pandas ---
# Integer Index: index = [0, 1]
# String Index: index = ['x', 'y']
# Datetime Index: index = pd.to_datetime(['2023-01-01', '2023-01-02'])


# --- Series ---
# Create a simple Series with custom index labels
s = pd.Series(data=[1, 2, 3], index=['a', 'b', 'c'])

# Display the Series
print(s)


# --- DataFrame ---
# Create a DataFrame from a dictionary with default integer index
df = pd.DataFrame(data={
    'First name': ['John', 'Jim', 'Jack'],
    'Last name': ['Doe', 'Evans', 'Farber'],
    'Age': [29, 45, 37]
})

# Display the DataFrame
print(df)

# Create the same DataFrame but with a custom row index
df = pd.DataFrame(data={
    'First name': ['John', 'Jim', 'Jack'],
    'Last name': ['Doe', 'Evans', 'Farber'],
    'Age': [29, 45, 37]
}, index=[1, 2, 3])

# Display the DataFrame with custom row index
print(df)

# Create a DataFrame from a list of lists with custom row index and column names
df = pd.DataFrame(
    data=[
        ['John', 'Doe', 29],
        ['Jim', 'Evans', 45],
        ['Jack', 'Farber', 37]
    ],
    index=[1, 2, 3],
    columns=['First name', 'Last name', 'Age']
)

# Display the final DataFrame
print(df)


# --- Footer ---
"""
🐼 Pandas Handbook by Pymetheus

🔗 Official Pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/

📘 Explore the interactive set of jupyter notebooks:
https://github.com/Pymetheus/pandas-handbook/notebooks
"""

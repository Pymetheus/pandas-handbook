# --- Pandas Handbook: 06 - Data Modifying ---
# Demonstrates data modifying techniques using the Titanic dataset


# --- Import Libraries ---
# Import pandas and numpy for data handling and os for path operations
import pandas as pd
import numpy as np
import os

# --- Load Dataset ---
# Set the path to the cleaned Titanic CSV file and load it into a DataFrame with PassengerId as index
data_processed = "../data/processed/"
csv_file = "clean_titanic.csv"
import_path = os.path.join(data_processed, csv_file)
df = pd.read_csv(import_path, index_col="PassengerId")

# --- Filter dataset for passengers with 'Mrs.' in their name ---
# Create a copy of the DataFrame and filter rows where 'Name' contains 'Mrs.'
mrs_df = df.copy()
mrs_filter = mrs_df['Name'].str.contains('Mrs.')
mrs_df = mrs_df[mrs_filter]

# --- Inserting or Dropping Columns ---
# Insert a new column 'Family Size' at position 5 as the sum of 'SibSp' and 'Parch'
mrs_df.insert(5, 'Family Size', mrs_df['SibSp'] + mrs_df['Parch'])
print(mrs_df.head(3))

# Insert a new boolean column 'Minor' at position 5 indicating if 'Age' is less than 18
mrs_df.insert(5, 'Minor', mrs_df['Age'] < 18)
print(mrs_df.head())

# Drop the 'Minor' column inplace
mrs_df.drop(columns='Minor', inplace=True)
print(mrs_df.head(3))

# Drop multiple specified columns inplace
mrs_df.drop(columns=['Survived', 'Pclass', 'Family Size', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], inplace=True)
print(mrs_df.head(3))

# --- Splitting & Extracting Values ---
# Create a copy of the original DataFrame and extract maiden names enclosed in parentheses into a new column
maiden_df = df.copy()
maiden_df['Maiden Name'] = maiden_df['Name'].str.extract(r'\(([^)]+)\)')
print(maiden_df[['Name', 'Maiden Name']].head(3))

# Split the 'Name' column of mrs_df into 'Surname' and 'Rest' using comma delimiter
mrs_df[['Surname', 'Rest']] = mrs_df['Name'].str.split(',', expand=True)

# Further split the 'Rest' column to extract 'Title' and the remaining string
mrs_df[['Title', 'Rest']] = mrs_df['Rest'].str.split('.', n=1, expand=True)

# Further split 'Rest' to extract 'Husband' and the remaining string
mrs_df[['Husband', 'Rest']] = mrs_df['Rest'].str.split('(', n=1, expand=True)

print(mrs_df.head())

# Clean up 'Rest' column by removing closing parenthesis
mrs_df['Rest'] = mrs_df['Rest'].str.replace(')', '')

# Replace empty or whitespace-only 'Husband' entries with 'Unknown'
mrs_df['Husband'] = mrs_df['Husband'].replace(r'^\s*$', 'Unknown', regex=True)
print(mrs_df.head())

# --- Merging Columns ---
# Create a new column 'Husband Fullname' by concatenating 'Surname' and 'Husband' with a comma separator
mrs_df['Husband Fullname'] = mrs_df['Surname'] + ',' + mrs_df['Husband']
print(mrs_df.head(3))

# --- Renaming and Formatting ---
# Rename the 'Rest' column to 'Maiden Name'
mrs_df.rename(columns={'Rest': 'Maiden Name'}, inplace=True)
print(mrs_df.head(3))

# Explicitly set new column names for the DataFrame
mrs_df.columns = ['Name', 'Gender', 'Age', 'Surname', 'Maiden Name', 'Title', 'Husband', 'Husband Fullname']
print(mrs_df.head(3))

# --- Modifying Column Strings ---
# Convert all column names to lowercase
mrs_df.columns = [x.lower() for x in mrs_df.columns]
print(mrs_df.head(3))

# Replace spaces with underscores in column names
mrs_df.columns = mrs_df.columns.str.replace(" ", "_")
print(mrs_df.head(3))

# Convert all values in the 'gender' column to uppercase
mrs_df['gender'] = mrs_df['gender'].str.upper()
print(mrs_df.head(3))

# --- Applying Custom Functions ---
# Apply the string lower() function to the 'gender' column
mrs_df['gender'] = mrs_df['gender'].apply(str.lower)
print(mrs_df.head(3))

# Define a function to convert strings to title case
def function_name(variable):
    return variable.title()

# Apply the custom function to the 'gender' column
mrs_df['gender'] = mrs_df['gender'].apply(function_name)
print(mrs_df.head(3))

# Apply a lambda function to convert 'gender' column entries to lowercase again
mrs_df['gender'] = mrs_df['gender'].apply(lambda x: x.lower())
print(mrs_df.head(3))

# Replace specific surnames with abbreviations in the 'surname' column
mrs_df['surname'] = mrs_df['surname'].replace({'Cumings': 'C.', 'Futrelle': 'F.'})
print(mrs_df.head(3))

# Map 'female' values to 'F' in the 'gender' column
mrs_df['gender'] = mrs_df['gender'].map({'female': 'F'})
print(mrs_df.head(3))

# --- Conditional Modifications ---
# Create a boolean filter for rows where 'surname' equals 'C.'
a_filter = mrs_df['surname'] == 'C.'

# Set 'title' to 'Lady' for rows matching the filter
mrs_df.loc[a_filter, 'title'] = 'Lady'
print(mrs_df.head(3))

# Set 'age' to NaN for rows where 'age' is 37 or higher
mrs_df['age'] = mrs_df['age'].where(mrs_df['age'] < 37, other=np.nan)
print(mrs_df.head(3))

# Restrict 'age' values to be between 25 and 35 inclusive
mrs_df['age'] = mrs_df['age'].clip(lower=25, upper=35)
print(mrs_df.head())

# --- Modifying by Index or Label ---
# Replace all values in the row with index 1
mrs_df.loc[1] = ['Elisabth', 'female', 27, 'Queens', 'Mary Stone', 'Mrs', 'Jake', 'Jake Queen']
print(mrs_df.tail())

# Update the 'age' value for the row with index 2
mrs_df.loc[2, 'age'] = 24
print(mrs_df.head(3))

# Update multiple columns 'age' and 'title' for the row with index 4
mrs_df.loc[4, ['age', 'title']] = [37, 'Lady']
print(mrs_df.head(3))

# Assign a list to a single cell at index 9 and column 'husband' (note: this creates a cell with a list)
mrs_df.at[9, 'husband'] = ['Oscar', 'W', 'ayne']
print(mrs_df.head(3))


# --- Footer ---
"""
🐼 Pandas Handbook by Pymetheus

🔗 Official Pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/

📘 Explore the interactive set of jupyter notebooks:
https://github.com/Pymetheus/pandas-handbook/notebooks

🔗 Explore the Titanic Dataset:
https://www.kaggle.com/competitions/titanic/data
"""

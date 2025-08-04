# --- Pandas Handbook: 07 - Data Combining - Concatenation, Merging & Joining ---
# Demonstrates data combining techniques using the Titanic dataset


# --- Import Libraries ---
# Import pandas for data handling and os for path operations
import pandas as pd
import os


# --- Load Dataset ---
# Define the file path and load the CSV into a DataFrame with PassengerId as index
data_processed = "../data/processed/"
csv_file = "clean_titanic.csv"
import_path = os.path.join(data_processed, csv_file)
df = pd.read_csv(import_path, index_col="PassengerId")


# --- Concatenation ---
# Split the DataFrame into two parts and concatenate them vertically (row-wise)
df1 = df.iloc[:450]
df2 = df.iloc[450:]

concat_df = pd.concat([df2, df1])
print(concat_df.head(3))

# Concatenate two DataFrames horizontally (column-wise) using selected columns
names = df[['Name']]
ages = df[['Age']]

concat_df = pd.concat([names, ages], axis=1)
print(concat_df.head(3))


# --- Merging ---
# Create a new DataFrame indicating if fare was over 100, then merge on PassengerId
extra_info = pd.DataFrame(data={'Overpaid': df['Fare'] > 100}, index=df.index)
merged_df = pd.merge(df, extra_info, on='PassengerId')
print(merged_df.head(3))


# --- Join Types: inner, outer, left, right ---
# Prepare two smaller DataFrames for merging examples
left_df = df[['Name']].iloc[:5]
right_df = df[['Age']].iloc[3:8]

# Inner merge: only rows with matching PassengerId in both DataFrames
inner_merge_df = pd.merge(left_df, right_df, on='PassengerId', how='inner')
print(inner_merge_df.head())

# Outer merge: all PassengerId values from both DataFrames, fill missing with NaN
outer_merge_df = pd.merge(left_df, right_df, on='PassengerId', how='outer')
print(outer_merge_df.head())

# Left merge: all PassengerId values from left_df, matched data from right_df
left_merge_df = pd.merge(left_df, right_df, on='PassengerId', how='left')
print(left_merge_df.head())

# Right merge: all PassengerId values from right_df, matched data from left_df
right_merge_df = pd.merge(left_df, right_df, on='PassengerId', how='right')
print(right_merge_df)


# --- Joining ---
# Extract titles from the 'Name' column and join them to the original DataFrame using the index
titles = df['Name'].str.extract(r'(Mr\.|Mrs\.|Miss\.|Lady\.)')
titles.columns = ['Title']
titles.index = df.index

joined_df = df.join(titles, on='PassengerId')
print(joined_df.head(3))


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

# --- Pandas Handbook: 05 - Data Cleaning ---
# Demonstrates data cleaning techniques using the Titanic dataset


# --- Import Libraries ---
# Import pandas and numpy for data handling and os for path operations
import pandas as pd
import numpy as np
import os


# --- Load Dataset ---
# Define path and load the CSV file into a DataFrame
data_raw = "../data/raw/"
csv_file = "titanic.csv"
import_path = os.path.join(data_raw, csv_file)

# Load dataset with PassengerId as index
df = pd.read_csv(import_path, index_col="PassengerId")


# --- Inspecting Missing Data ---
# Show first 3 rows to get a glimpse of the dataset
print(df.head(3))

# Show concise summary including data types and non-null counts
print(df.info())

# Show which entries are missing values for first 3 rows
print(df.isna().head(3))

# Show first 3 rows where Age is missing
print(df[df['Age'].isna()].head(3))

# Count missing values per column
print(df.isna().sum())

# Count total missing values in entire DataFrame
print(df.isna().sum().sum())

# Show first 3 rows with any missing value
print(df[df.isna().any(axis=1)].head(3))

# Show rows where all values are missing (should be empty here)
print(df[df.isna().all(axis=1)])

# Count rows with any missing data
print(len(df[df.isna().any(axis=1)]))

# Filter rows where both Age and Cabin are missing, then describe
without_age_cabin = df[df['Age'].isna() & df['Cabin'].isna()]
print(without_age_cabin.describe())

# Check if first passenger's Cabin value is NaN
first_passenger = df.loc[1, "Cabin"]
print(pd.isna(first_passenger))

# Check if first passenger's Cabin value is NOT NaN
print(pd.notna(first_passenger))


# --- Handling Missing Data on Import ---
# Load CSV disabling default NA value recognition (keep all strings as-is)
a_df = pd.read_csv(import_path, index_col="PassengerId", keep_default_na=False)
print(a_df.info())

# Define additional strings to treat as NaN
na_vals = ["C", "Missing"]

# Load CSV treating 'C' and 'Missing' as NaN
b_df = pd.read_csv(import_path, index_col="PassengerId", na_values=na_vals)
print(b_df.info())

# Check unique values in 'Embarked' column
print(b_df['Embarked'].unique())

# Replace 'Q' in Embarked column with NaN
b_df.replace('Q', np.nan, inplace=True)

# Check unique values after replacement
print(b_df['Embarked'].unique())


# --- Cleaning Data Types ---
# Create a copy for cleaning
c_df = df.copy()

# Show data types of all columns
print(c_df.dtypes)

# Show first 3 rows of all int columns
print(c_df.select_dtypes(include=['int']).head(3))

# Show first 3 rows of all non-object columns
print(c_df.select_dtypes(exclude=['object']).head(3))

# Convert 'Survived' column to string type
c_df['Survived'] = c_df['Survived'].astype(str)

# Verify data types after conversion
print(c_df.dtypes)

# Convert 'Survived' back to numeric
c_df['Survived'] = pd.to_numeric(c_df['Survived'])

# Verify data types after reconversion
print(c_df.dtypes)


# --- Dropping Missing or Unwanted Data ---
# Copy dataset and drop row with index label 1
drop_a_df = df.copy()
print(drop_a_df.drop(index=1).head(3))

# Drop all rows with any missing value
drop_b_df = df.copy()
print(drop_b_df.dropna(axis=0).head(3))

# Drop all columns with any missing value
drop_c_df = df.copy()
print(drop_c_df.dropna(axis=1).head(3))

# Drop rows where both Age and Cabin are missing (all missing)
drop_d_df = df.copy()
print(drop_d_df.dropna(axis='index', how='all', subset=['Age', 'Cabin']).head(3))

# Drop rows where any of Age or Cabin is missing
drop_e_df = df.copy()
print(drop_e_df.dropna(axis='index', how='any', subset=['Age', 'Cabin']).head(3))

# Drop 'Age' and 'Cabin' columns from dataset
drop_f_df = df.copy()
drop_f_df.drop(columns=['Age', 'Cabin'], inplace=True)
print(drop_f_df.head(3))

# Duplicate dataset by concatenation, then drop duplicates
drop_g_df = df.copy()
drop_g_df = pd.concat([drop_g_df, drop_g_df])
print(len(drop_g_df))  # Expect 1782
drop_g_df.drop_duplicates(inplace=True)
print(len(drop_g_df))  # Back to 891

# Drop all rows where 'Survived' equals 0 (filtering for survivors)
survived_df = df.copy()
dead_filter = survived_df['Survived'] == 0
print(survived_df.drop(index=survived_df[dead_filter].index).head(3))


# --- Filling Missing Data ---
# Fill all missing values with 0
fill_a_df = df.copy()
print(fill_a_df.fillna(0).head(3))

# Fill missing values in 'Age' column with 0, inplace
fill_b_df = df.copy()
fill_b_df.fillna({'Age': 0}, inplace=True)
print(fill_b_df.head(6))


# --- Detecting and Cleaning Invalid Categorical Values ---
# Copy dataset and show unique values in 'Sex' column
san_a_df = df.copy()
print(san_a_df['Sex'].unique())

# Standardize 'Sex' values by stripping whitespace, lowering, then title casing
san_a_df['Sex'] = san_a_df['Sex'].str.strip().str.lower().str.title()
print(san_a_df['Sex'].unique())

# Create copy and replace 'male' with blank space in 'Sex' column
san_b_df = df.copy()
san_b_df['Sex'] = san_b_df['Sex'].replace({'male': ' '})
print(san_b_df.head(3))

# Replace blank or whitespace entries in 'Sex' column with 'Male'
san_b_df['Sex'] = san_b_df['Sex'].replace(r'^\s*$', 'Male', regex=True)
print(san_b_df.head(3))


# --- Cleaning the Age Column ---
# Display mean age of dataset
print(df['Age'].mean())

# Display median age of dataset
print(df['Age'].median())

# Filter rows where Age is missing and show first 3
without_age_df = df.copy()
without_age_filter = without_age_df['Age'].isna()
print(without_age_df[without_age_filter].head(3))

# Fill missing Age values with median Age
clean_median_age_df = df.copy()
clean_median_age_df.fillna({'Age': clean_median_age_df['Age'].median()}, inplace=True)
print(clean_median_age_df.isna().sum())

# Fill missing Age values with mean Age
clean_mean_age_df = df.copy()
clean_mean_age_df.fillna({'Age': clean_mean_age_df['Age'].mean()}, inplace=True)
print(clean_mean_age_df.isna().sum())

# Fill missing Age values grouped by Survived, Pclass, and Sex using group median
clean_related_age_df = df.copy()
relation_filter = ['Survived', 'Pclass', 'Sex']
clean_related_age_df['Age'] = clean_related_age_df.groupby(relation_filter)['Age'].transform(lambda x: x.fillna(x.median()))
print(clean_related_age_df.isna().sum())

# Drop all rows where Age is missing
clean_droped_df = df.copy()
clean_droped_df = clean_droped_df.dropna(subset=['Age'])
print(clean_droped_df.isna().sum())


# --- Comparing Cleaned Age Data ---
print(f"Raw data set median age: >> {df['Age'].median()} << vs mean: >> {df['Age'].mean()} <<")
print(f"Clean median data set median age: >> {clean_median_age_df['Age'].median()} << vs mean: >> {clean_median_age_df['Age'].mean()} <<")
print(f"Clean mean data set median age: >> {clean_mean_age_df['Age'].median()} << vs mean: >> {clean_mean_age_df['Age'].mean()} <<")
print(f"Clean related data set median age: >> {clean_related_age_df['Age'].median()} << vs mean: >> {clean_related_age_df['Age'].mean()} <<")
print(f"Clean droped data set median age: >> {clean_droped_df['Age'].median()} << vs mean: >> {clean_droped_df['Age'].mean()} <<")


# --- Cleaning the Cabin Column ---
# Filter rows where Cabin is missing and show first 3
clean_cabin_df = df.copy()
without_cabin_filter = clean_cabin_df['Cabin'].isna()
print(clean_cabin_df[without_cabin_filter].head(3))

# Replace missing Cabin values with 'Unknown'
clean_cabin_df['Cabin'] = clean_cabin_df['Cabin'].fillna('Unknown')
print(clean_cabin_df.head(3))


# --- Cleaning the Embarked Column ---
# Filter rows where Embarked is missing
without_embarked_df = df.copy()
without_embarked_filter = without_embarked_df['Embarked'].isna()
print(without_embarked_df[without_embarked_filter])

# Check if missing Embarked rows have Cabin containing 'B2'
cabin_filter = without_embarked_df['Cabin'].fillna('Unknown').str.contains('B2')
print(without_embarked_df[cabin_filter])

# Check if missing Embarked rows have Ticket containing '1135'
ticket_filter = without_embarked_df['Ticket'].fillna('Unknown').str.contains('1135')
print(without_embarked_df[ticket_filter])

# Check if missing Embarked rows have names containing specific keywords
icard_filter = without_embarked_df['Name'].fillna('Unknown').str.contains('Icard')
stone_filter = without_embarked_df['Name'].fillna('Unknown').str.contains('Stone')
evelyn_filter = without_embarked_df['Name'].fillna('Unknown').str.contains('Evelyn')
print(without_embarked_df[icard_filter])
print(without_embarked_df[stone_filter])
print(without_embarked_df[evelyn_filter])

# Fill missing Embarked values with 'S' (most common port)
clean_embarked_df = df.copy()
clean_embarked_df['Embarked'] = clean_embarked_df['Embarked'].fillna('S')
print(clean_embarked_df['Embarked'].isna().sum())


# --- Final data inspection ---
print(clean_embarked_df.info())
print(clean_embarked_df.head(3))


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

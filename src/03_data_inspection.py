# --- Pandas Handbook: 03 - Data Inspection ---
# Demonstrates data inspection techniques using the Ramen Ratings dataset

# --- Import Libraries ---
# Import pandas for data handling and os for path operations
import pandas as pd
import os


# --- Load Dataset ---
# Set path variables for raw data and define the CSV filename
data_raw = "../data/raw/"
csv_file = "ramen-ratings.csv"

# Build the full import path and load the CSV into a DataFrame using 'Review #' as the index column
import_path = os.path.join(data_raw, csv_file)
df = pd.read_csv(import_path, index_col='Review #')


# --- Basic Dataset Overview ---
# Display the first 5 rows of the DataFrame
print(df.head())

# Display the last 5 rows of the DataFrame
print(df.tail())

# Display the shape of the DataFrame (rows, columns)
print(df.shape)

# Display the column names
print(df.columns)

# Display the DataFrame index
print(df.index)

# Show the data types of each column
print(df.dtypes)

# Provide concise summary of DataFrame including non-null counts and memory usage
print(df.info())

# Display memory usage per column in bytes
print(df.memory_usage())


# --- Missing & Null Values ---
# Show the number of missing (NaN) values per column
print(df.isnull().sum())

# Show the number of missing (NaN) values per column (alternative method)
print(df.isna().sum())

# Count non-null values in the 'Top Ten' column
print(df['Top Ten'].count())

# Return DataFrame showing True for non-null and False for null values
print(df.notnull())


# --- Column-Level Inspection ---
# Count of unique values in 'Brand' column sorted descending
print(df['Brand'].value_counts())

# Count of empty strings in 'Brand' column after stripping whitespace
print((df['Brand'].str.strip() == '').sum())

# Apply the len() function to each value in 'Stars' column
print(df['Stars'].apply(len))

# List unique values in 'Style' column
print(df['Style'].unique())

# Number of unique values in 'Style' column
print(df['Style'].nunique())

# Random sample from 'Variety' column
print(df['Variety'].sample())


# --- Sorting & Ordering ---
# Sort DataFrame by 'Country' column in ascending order and show top 3 rows
print(df.sort_values('Country', ascending=True).head(3))

# Sort DataFrame by index in ascending order and show top 3 rows
print(df.sort_index(ascending=True).head(3))


# --- Descriptive Statistics ---
# Generate descriptive statistics for numeric columns (though none yet)
print(df.describe())

# Replace 'Unrated' with 0 in 'Stars' column and convert to float for numeric analysis
stars_df = df['Stars'].replace('Unrated', 0).astype(float)

# Calculate mean of the 'Stars' column
print(stars_df.mean())

# Calculate median of the 'Stars' column
print(stars_df.median())

# Calculate standard deviation of the 'Stars' column
print(stars_df.std())

# Calculate 0.5 quantile (median) of the 'Stars' column
print(stars_df.quantile())

# Calculate sum of the 'Stars' column
print(stars_df.sum())

# Calculate cumulative sum of the 'Stars' column
print(stars_df.cumsum())

# Calculate variance of the 'Stars' column
print(stars_df.var())

# Find minimum value in the 'Stars' column
print(stars_df.min())

# Find maximum value in the 'Stars' column
print(stars_df.max())

# Return top 5 rows with largest values in 'Stars'
print(stars_df.nlargest(5))

# Return top 5 rows with smallest values in 'Stars'
print(stars_df.nsmallest(5))


# --- Combining Data Inspection Methods ---
# Count frequency of each star rating in descending order by rating
stars_val_count = stars_df.value_counts()
print(stars_val_count.sort_index(ascending=False).head())

# Count frequency of each star rating sorted by count descending
print(stars_val_count.sort_values(ascending=False).head())


# --- Footer ---
"""
🐼 Pandas Handbook by Pymetheus

🔗 Official Pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/

📘 Explore the interactive set of jupyter notebooks:
https://github.com/Pymetheus/pandas-handbook/notebooks

🔗 Explore the Ramen Ratings Dataset:
https://www.kaggle.com/datasets/residentmario/ramen-ratings/data
"""

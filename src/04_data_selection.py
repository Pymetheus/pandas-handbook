# --- Pandas Handbook: 04 - Data Selection ---
# Demonstrates data selection techniques using the Ramen Ratings dataset


# --- Import Libraries ---
# Import pandas for data handling and os for path operations
import pandas as pd
import os


# --- Load Dataset ---
# Define path and load the CSV file into a DataFrame
data_raw = "../data/raw/"
csv_file = "ramen-ratings.csv"
import_path = os.path.join(data_raw, csv_file)
df = pd.read_csv(import_path)


# --- Set & Reset Index ---
# Set 'Review #' as the index of the DataFrame
df.set_index('Review #', inplace=True)

# Show the DataFrame with default integer index (without modifying original)
print(df.reset_index(inplace=False).head(3))

# Show first 3 rows of current DataFrame (with 'Review #' as index)
print(df.head(3))

# --- Select Data by Label or Position ---
# Select data by integer position (row 0, column 0)
print(df.iloc[0, 0])

# Access a single value by position using iat (row 0, column 0)
print(df.iat[0, 0])

# Select data by label: row with index 2580, column 'Variety'
print(df.loc[2580, 'Variety'])

# Access single value by label with at
print(df.at[2580, 'Variety'])


# --- Select Multiple Rows & Columns ---
# Select multiple rows and columns by integer positions
print(df.iloc[[0, 1], [0, 1, 2]])

# Select multiple rows and columns by index and column labels
print(df.loc[[2580, 2579], ['Brand', 'Variety', 'Style']])


# --- Slice the DataFrame ---
# Slice rows by position: rows 10 to 12 (stop exclusive)
print(df[10:13])

# Select single column by name (first 3 rows)
print(df['Country'].head(3))

# Select multiple columns by name (first 3 rows)
print(df[['Brand', 'Variety', 'Style']].head(3))

# Select multiple columns safely using get (first 3 rows)
print(df.get(['Brand', 'Variety', 'Style']).head(3))

# Select column using dot notation (first 3 rows)
print(df.Country.head(3))


# --- Slice by Label with df.loc[] ---
# Slice rows and columns by label; note end label is inclusive
print(df.loc[2580:2579, 'Brand':'Style'])

# Select all rows and specific columns by name (first 3 rows)
print(df.loc[:, ['Brand', 'Variety', 'Style']].head(3))


# --- Select with Conditions ---
# Select columns whose names contain 'y' (first 3 rows)
print(df.loc[:, df.columns.str.contains('y')].head(3))

# Filter rows where 'Country' is either 'Japan' or 'South Korea' (first 3 rows)
print(df[df['Country'].isin(['Japan', 'South Korea'])].head(3))

# Filter rows where 'Brand' is 'Yamachan' (first 3 rows)
brand_yamachan = df[df['Brand'] == 'Yamachan']
print(brand_yamachan.head(3))

# Further filter the previous selection by 'Stars' > 4.5 (casting Stars to float)
print(brand_yamachan[brand_yamachan['Stars'].astype(float) > 4.5])


# --- Logical Operators in Pandas ---
# <, >, ==, <=, >=, !=, &, |, ~
# These can be combined with boolean masks or inside .query() for filtering


# --- Select with Query ---
# Create a copy of df and convert 'Stars' column to float after replacing 'Unrated' with 0
query_df = df.copy()
query_df['Stars'] = query_df['Stars'].replace('Unrated', 0).astype(float)

# Query rows where Country is 'Japan' and Stars >= 4.5 (first 3 rows)
print(query_df.query("Country == 'Japan' and Stars >= 4.5").head(3))

# Query rows where Country is in the list ['Japan', 'Taiwan'] (first 3 rows)
print(query_df.query("Country in ['Japan', 'Taiwan']").head(3))


# --- Select with Regex ---
# Select columns with names matching regex 'C' (first 5 rows)
print(df.filter(regex='C').head())


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

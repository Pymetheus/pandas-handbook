# --- Pandas Handbook: 02 - Importing & Exporting Data ---
# Demonstrates importing & exporting data using the Ramen Ratings dataset

# --- Import Libraries ---
# Import core libraries: pandas for data handling, and os/sys for file path management.
import pandas as pd
import sys
import os


# --- Load Dataset ---
# Define paths and filenames for all supported data formats (CSV, Excel, JSON, HTML, SQL, Parquet, Feather, HDF5).
sys.path.append(os.path.abspath(".."))

data_raw = "../data/raw/"
data_processed = "../data/processed/"

csv_file = "ramen-ratings.csv"
tsv_file = "ramen-ratings.tsv"
excel_file = "ramen-ratings.xlsx"  # Requires the openpyxl library installed
json_file = "ramen-ratings.json"
html_file = "ramen-ratings.html"  # Requires the lxml library installed

database = "sqlite:///../data/sample_database.db"  # Requires the SQLAlchemy library installed
sql_table = "sample_table"

parquet_file = "ramen-ratings.parquet"  # Requires the pyarrow library installed
feather_file = "ramen-ratings.feather"  # Requires the pyarrow library installed
hdf_file = "ramen-ratings.h5"  # Requires the pytables library installed


# --- From and To CSV ---
# Load CSV into a DataFrame and display the first 5 rows
import_path = os.path.join(data_raw, csv_file)
df = pd.read_csv(import_path)

print(df.head())

# Export DataFrame to CSV without index
export_path = os.path.join(data_processed, csv_file)
df.to_csv(export_path, index=False)

# Read CSV again with "Review #" as the index column and display first 5 rows
df = pd.read_csv(import_path, index_col='Review #')

print(df.head())

# Export DataFrame to CSV including the index column
export_path = os.path.join(data_processed, csv_file)
df.to_csv(export_path)

# Export CSV with tab-separated values (TSV)
export_path = os.path.join(data_processed, tsv_file)
df.to_csv(export_path, sep='\t')


# --- From and To Excel ---
# Read Excel file and set "Review #" as the index column, then display first 5 rows
import_path = os.path.join(data_raw, excel_file)
df = pd.read_excel(import_path, index_col='Review #')

print(df.head())

# Export DataFrame to Excel file
export_path = os.path.join(data_processed, excel_file)
df.to_excel(export_path)


# --- From and To JSON ---
# Read JSON file into a DataFrame and display first 5 rows
import_path = os.path.join(data_raw, json_file)
df = pd.read_json(import_path)

print(df.head())

# Export DataFrame to JSON file
export_path = os.path.join(data_processed, json_file)
df.to_json(export_path)


# --- From and To HTML ---
# Read tables from HTML file; pd.read_html() returns a list of DataFrames
import_path = os.path.join(data_raw, html_file)
df_list = pd.read_html(import_path)

# Display first 5 rows of the first table
print(df_list[0].head())

# Export the first HTML table (DataFrame) to an HTML file without the index
export_path = os.path.join(data_processed, html_file)
df_list[0].to_html(export_path, index=False)


# --- From and To SQL ---
# Import create_engine from SQLAlchemy and set up connection to SQLite database
from sqlalchemy import create_engine
engine = create_engine(database)

# Read a SQL table into a DataFrame and set "Review #" as the index
df = pd.read_sql(sql_table, engine, index_col='Review #')
print(df.head())

# Export DataFrame to SQL table, replacing it if it already exists
df.to_sql(sql_table, engine, if_exists='replace')


# --- From and To Parquet, Feather and HDF ---

# From and To Parquet
# Read a Parquet file into a DataFrame and display first 5 rows
import_path = os.path.join(data_raw, parquet_file)
df = pd.read_parquet(import_path)

print(df.head())

# Export DataFrame to Parquet with Snappy compression
export_path = os.path.join(data_processed, parquet_file)
df.to_parquet(export_path, engine='pyarrow', compression='snappy')

# From and To Feather
# Read a Feather file into a DataFrame and display first 5 rows
import_path = os.path.join(data_raw, feather_file)
df = pd.read_feather(import_path)

print(df.head())

# Export DataFrame to Feather file
export_path = os.path.join(data_processed, feather_file)
df.to_feather(export_path)

# From and To HDF
# Read from HDF5 file using a specific key and display first 5 rows
import_path = os.path.join(data_raw, hdf_file)
df = pd.read_hdf(import_path, key='df')

print(df.head())

# Export DataFrame to HDF5 file with compression
export_path = os.path.join(data_processed, hdf_file)
df.to_hdf(export_path, key='df', mode='w', format='table', complib='blosc', complevel=9)


# --- Comparing File Sizes ---
# Measure and print file size (in KB) of each saved file, sorted from smallest to largest
from pathlib import Path

folder = Path(data_processed)
file_dict = {}

for file in folder.iterdir():
    if file.is_file():
        size_kb = file.stat().st_size / 1024
        file_dict[file.name] = round(size_kb, 2)

sorted_dict = dict(sorted(file_dict.items(), key=lambda item: item[1]))

for key, value in sorted_dict.items():
    # Extract file extension and title-case it for display
    ext = key.split('.')[-1].title()
    print(f"File: {ext} with size: {value}")


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

![Pandas Handbook](res/pandas-handbook.png)

<h1 align="center">
    🐼 Pandas Handbook
</h1>

Welcome to the **Pandas Handbook**! 
This project is a collection of [Jupyter notebooks](notebooks) and corresponding [Python scripts](src) 
designed to help you learn and master the [pandas](https://pandas.pydata.org/) library for data analysis and manipulation in Python. 
Each notebook covers a core aspect of working with pandas, with hands-on examples and practical workflows.

---

## Table of Contents
- [Intro](#intro)
- [Getting Started](#getting-started)
- [The Pandas Handbook](#the-pandas-handbook)
  - [00 General](#00-general)
  - [01 Data Structures](#01-data-structures)
  - [02 Importing & Exporting Data](#02-importing--exporting-data)
  - [03 Data Inspection](#03-data-inspection)
  - [04 Data Selection](#04-data-selection)
  - [05 Data Cleaning](#05-data-cleaning)
  - [06 Data Modifying](#06-data-modifying)
  - [07 Data Combining](#07-data-combining)
  - [08 Data Analyzing](#08-data-analyzing)
  - [09 Dates & Time Series](#09-dates--time-series)
  - [10 Plotting & Visualization](#10-plotting--visualization)
- [Who this is for](#who-this-is-for)
- [Datasets used](#datasets-used)
- [Contributing](#contributing)
- [License](#license)

---

## Intro
The **Pandas Handbook** is a practical, example-driven guide to mastering the pandas library for data analysis and manipulation in Python. 
Whether you’re just starting out or looking to deepen your understanding, 
this collection of Jupyter notebooks walks you through the essential workflows and features of pandas 
using real-world datasets and clear, concise explanations. 
Each notebook builds on the last, helping you learn pandas step by step—from loading and 
inspecting data to cleaning, transforming, analyzing, and visualizing it. 
Perfect for students, data enthusiasts, and professionals alike!

---

## Getting Started
1. **Clone this repository:**
   ```bash
   git clone https://github.com/Pymetheus/pandas-handbook.git
   ```

2. **Install requirements:**
   ```bash
   cd pandas-handbook/dep
   pip install -r requirements.txt
   ```
3. **Start Jupyter Notebook:**
   ```bash
   cd pandas-handbook/notebooks    
   jupyter notebook
   ```
   Open the desired notebook in your browser and follow along!

---

## The Pandas Handbook

### 00 General
Introduces the pandas library, how to install it, and how to start using it in your Python projects.  

```pip install pandas``` – Install pandas using [pip](https://pypi.org/project/pandas/).  
```import pandas as pd``` – Pandas is commonly imported as pd to make code shorter and easier to read.  
```print(pd.__version__)``` – Check the installed pandas version.  
```help(pd.DataFrame)``` – Learn how pandas functions and objects work.

👉 Check out more in the [Jupyter notebook](notebooks/00-general.ipynb) or [Python Script](src/00_general.py).  

---
### 01 Data Structures
Explains the core pandas data structures—Series and DataFrame—and their underlying index types.  

```pd.Series(data=[VALUE, VALUE, VALUE], index=[1, 2, 3])``` – Create a simple Series with custom index labels.  
```pd.DataFrame(data={'KEY': ['VALUE', 'VALUE', 'VALUE']}, index=[1, 2, 3])``` – Create a DataFrame with a custom row index.

👉 Check out more in the [Jupyter notebook](notebooks/01-data-structures.ipynb) or [Python Script](src/01_data_structures.py).  

---
### 02 Importing & Exporting Data
Shows how to read data from and write data to various file formats (CSV, Excel, JSON, etc.) with pandas.  

#### 📄 From and to CSV
```pd.read_csv(import_path)``` – Read data from a CSV file.  
```df.to_csv(export_path)``` – Write the DataFrame to a CSV file.  

#### 📄 From and to Excel
```pd.read_excel(import_path, index_col='INDEX_COLUMN')``` – Read data from an Excel file and set the index.  
```df.to_excel(export_path)``` – Export the DataFrame to an Excel file. 

#### 📄 From and to JSON
```pd.read_json(import_path)``` – Read structured data from a JSON file into a DataFrame.  
```df.to_json(export_path)``` – Export the DataFrame to a JSON file.  

#### 📄 From and to SQL
```pd.read_sql(sql_table, engine, index_col='INDEX_COLUMN')``` – Read a SQL table into a DataFrame and set the index.  
```df.to_sql(sql_table, engine, if_exists='replace')``` – Write the DataFrame to the SQL table, replacing it if it already exists.  

👉 Check out more in the [Jupyter notebook](notebooks/02-import-export.ipynb) or [Python Script](src/02_import_export.py).  

---
### 03 Data Inspection
Teaches techniques to explore, summarize, and inspect datasets to better understand their structure and contents.  

#### 📌 Basic Dataset Overview
`df.head()` – Displays the first 5 rows of the DataFrame.  
`df.tail()` – Displays the last 5 rows of the DataFrame.  
`df.shape` – Returns the number of rows and columns as a tuple.  
`df.columns` – Lists the column names in the DataFrame.  
`df.index` – Shows the index (row labels) of the DataFrame.  
`df.dtypes` – Displays the data type of each column.  
`df.info()` – Provides a concise summary of the DataFrame, including column types, non-null counts, and memory usage.  
`df.memory_usage()` – Returns memory usage of each column, useful for optimization.  

#### 🔍 Missing & Null Values
`df.isnull().sum()` – Shows the number of missing values (`NaN`) per column.  
`df.isna().sum()` – Shows the number of missing values (`NaN`) per column.  
`df['COLUMN'].count()` – Counts non-null values in the specified `'COLUMN'`.  
`df.notnull()` – Returns a DataFrame of the same shape indicating whether each value is not null (`True`) or null (`False`).  

#### 🧬 Column-Level Inspection
`df['COLUMN'].value_counts()` – Returns a count of unique values in the specified `'COLUMN'`, sorted in descending order.  
`(df['COLUMN'].str.strip() == '').sum()` – Returns a count of empty strings in the specified `'COLUMN'`.  
`df['COLUMN'].apply(len)` – Applies the `len()` function to each value in the specified `'COLUMN'`.  
`df['COLUMN'].unique()` – Lists unique values in the specified `'COLUMN'`.  
`df['COLUMN'].nunique()` – Returns the number of unique values in the specified `'COLUMN'`.  
`df['COLUMN'].sample()` – Randomly samples one or more rows from the specified `'COLUMN'`.  

#### 🗂️ Sorting & Ordering
`df.sort_values('COLUMN')` – Sorts the DataFrame by values in the specified `'COLUMN'`.  
`df.sort_index()` – Sorts the DataFrame by its index values.  

#### 📊 Descriptive Statistics
`df.describe()` – Generates descriptive statistics for numeric columns.  
`df.mean()` – Calculates the mean of the specified data frame values.  
`df.median()` – Calculates the median of the specified data frame values.  
`df.std()` – Computes the standard deviation of the specified data frame values.  
`df.quantile()` – Returns the 0.5 quantile (default is median).  
`df.sum()` – Returns the sum of the specified data frame values.  
`df.cumsum()` – Computes the cumulative sum of the specified data frame values.  
`df.var()` – Calculates the variance of the specified data frame values.  
`df.min()` – Returns the minimum value in specified data frame.  
`df.max()` – Returns the maximum value in specified data frame.  
`df.nlargest(n, 'COLUMN')` – Returns the top `n` rows with the largest values in the specified 'COLUMN'.  
`df.nsmallest(n, 'COLUMN')` – Returns the top `n` rows with the smallest values in the specified 'COLUMN'.

👉 Check out more in the [Jupyter notebook](notebooks/03-data-inspection.ipynb) or [Python Script](src/03_data_inspection.py).  

---
### 04 Data Selection
Demonstrates ways to select, filter, and slice data in pandas, including label- and position-based indexing.  

#### 🎯 Select Data by Label or Position
`df.set_index('COLUMN', inplace=True)` – Sets the specified `'COLUMN'` as the DataFrame’s new index.  
`df.reset_index(inplace=True)` – Resets the index to default integers and moves the current index back to a column.  

`df.iloc[row_index, column_index]` – Selects data by **integer position** for rows and columns.  
`df.iat[row_index, column_index]` – Accesses a **single value** by position.  
`df.loc[index_label, column_label]` – Selects data by **label** for index and columns.  
`df.at[index_label, column_label]` – Accesses a **single value** by label.  

Use `df.loc[]` and `df.iloc[]` to select rows and columns by label or position.  
Use `df.at[]` and `df.iat[]` for fast access to a single value.  

`df.iloc[[row1, row2], [col1, col2]]` – Selects specific rows and columns by **position**.  
`df.loc[[index_label1, index_label2], ['col1', 'col2']]` – Selects specific index and columns by **label**.  

#### 🔢 Slice by Row Position or Column Name
`df[start:stop]` – Slices rows by position (stop is exclusive).  
`df['COLUMN']` – Selects a single column by name (returns a Series).  
`df[['COLUMN_1', 'COLUMN_2']]` – Selects multiple columns by name.  
`df.get(['COLUMN_1', 'COLUMN_1'])` – Selects safely multiple columns by name.  
`df.COLUMN` – Dot notation for selecting a column (if name is a valid Python identifier).  

#### 🏷️ Slice by Label with `df.loc[]`
`df.loc[start_label:end_label, 'COLUMN_1':'COLUMN_3']` – Slices rows and columns by label.  
`df.loc[:, ['COLUMN_1', 'COLUMN_2']]` – Selects all rows, and specific columns by name.  

#### 🔍 Select with Conditions
`df.loc[:, df.columns.str.contains('pattern')]` – Selects all columns whose name matches the regex `'pattern'`.  
`df[df['COLUMN'].isin(['VALUE_1', 'VALUE_2'])]` – Filters rows where the column value is in the given list.   
`df[df['COLUMN'] == 'VALUE']` – Selects rows where the specified column matches the condition.    
`df[df['COLUMN'] > NUM]` – Filters rows based on numeric comparison.    

#### 🔍 Select with Query
`df.query("COLUMN == 'VALUE' and COLUMN > num")` – Filters rows using a SQL-like expression with improved readability.  
`df.query("COLUMN in ['VALUE_1', 'VALUE_2']")` – Filters rows where the column matches a list of values.  

#### 🔍 Select with Regex
`df.filter(regex='pattern')` – Selects columns whose names match the given regular expression.

👉 Check out more in the [Jupyter notebook](notebooks/04-data-selection.ipynb) or [Python Script](src/04_data_selection.py).  

---
### 05 Data Cleaning
Covers methods for identifying and dealing with missing, invalid, or inconsistent data in real-world datasets.  

#### 🧼 Inspecting Missing Data  
```df.isna()``` – Returns a DataFrame of the same shape indicating where values are `NaN` (True = missing).   
```df[df['COLUMN'].isna()]``` – Filters rows where the specified column has missing values.   
```df.isna().sum()``` – Counts missing values per column.  
```df.isna().sum().sum()``` – Total count of missing values in entire DataFrame.   
```df[df.isna().any(axis=1)]``` – Filters rows with *any* missing values.   
```df[df.isna().all(axis=1)]``` – Filters rows where *all* columns are missing.   
```pd.isna(value)``` – Checks if a scalar value is NaN.   
```pd.notna(value)``` – Checks if a scalar value is *not* NaN.   

#### 📥 Handling Missing Data on Import
```pd.read_csv(filepath, keep_default_na=False)``` – Disables automatic conversion of certain strings (e.g., "NA", "NaN") to `NaN`.  
```pd.read_csv(filepath, na_values=['val1', 'val2'])``` – Specifies additional strings to treat as `NaN` during import.  
```df.replace('VALUE', np.nan, inplace=True)``` – Replaces specific values with `NaN` in-place.  

#### 🧽 Cleaning Data Types
```df.dtypes``` – Shows data types of each column.  
```df.select_dtypes(include=['type'])``` – Selects columns with a specific data type.  
```df.select_dtypes(exclude=['type'])``` – Excludes columns of a specific data type.  
```df['COLUMN'] = df['COLUMN'].astype('type')``` – Converts a column to the specified data type (e.g., `'int'`, `'float'`, `'object'`).  
```pd.to_numeric(df['COLUMN'])``` – Converts values to numbers.   

#### 🗑️ Dropping missing or unwanted data
```df.drop(index=LABEL)``` – Drops a row by index label.  
```df.dropna(axis=0)``` – Drops rows with *any* missing values.  
```df.dropna(axis=1)``` – Drops columns with *any* missing values.  
```df.dropna(how='all')``` – Drops rows/columns only if *all* values are missing.  
```df.dropna(subset=['COLUMN_1', 'COLUMN_2'], how='any')``` – Drops rows where *any* specified columns are missing.  
```df.drop(columns=['COLUMN_1', 'COLUMN_2'])``` – Drops specified columns.  
```df.drop_duplicates(inplace=True)``` – Removes duplicate rows in-place.  
```filter``` = ```df[df['COLUMN'] != value]``` – Filters rows where a column is *not* equal to a value.  
```df.drop(index=df[filter].index)```  – Drops rows which match the filter

#### 🧯 Filling Missing Data  
```df.fillna(0)``` – Replaces all missing values with `0`.  
```df.fillna({'COLUMN': VALUE})``` – Replaces missing values only in specified column(s).  
```df['COLUMN'].fillna(df['COLUMN'].mean())``` – Fills missing values in a column with the mean.  
```df['COLUMN'].fillna(df['COLUMN'].median())``` – Fills missing values with the median.  
```df.groupby(['COLUMN'])['TARGET_COLUMN'].transform(lambda x: x.fillna(x.median()))``` – Fills missing values with grouped medians.  

#### 🧯 Detecting and Cleaning Invalid Categorical Values
```df['COLUMN'].str.strip().str.lower().str.title()``` – Strips, lowers and titles data in a column.  
```df['COLUMN'].replace('invalid', np.nan, inplace=True)``` – Replaces invalid values with `NaN`.  
```df['COLUMN'] = df['COLUMN'].replace(r'^\s*$', np.nan, regex=True)``` – Replaces empty strings or whitespaces with `NaN`.

👉 Check out more in the [Jupyter notebook](notebooks/05-data-cleaning.ipynb) or [Python Script](src/05_data_cleaning.py).  

---
### 06 Data Modifying
Focuses on how to update, transform, and manipulate columns and values in your DataFrames.  

#### ➕ Inserting or Dropping Columns
```df.insert(POSITION, 'NEW_COLUMN', df['COLUMN1'] + df['COLUMN2'])``` – Inserts a new column at a specified position by summing two existing columns.  
```df.insert(POSITION, 'NEW_COLUMN', df['COLUMN'] < VALUE)``` – Inserts a new column based on a condition.  
```df.drop(columns='COLUMN', inplace=True)``` – Drops a single specified column in place.  
```df.drop(columns=['COLUMN_1', 'COLUMN_2', ...], inplace=True)``` – Drops multiple specified columns in place.

#### 🔪 Splitting & Extracting Values
```df['NEW_COLUMN'] = df['COLUMN'].str.extract(r'PATTERN')``` – Extracts substrings matching a regex pattern into a new column.  
```df[['NEW_COLUMN_1', 'NEW_COLUMN_2']] = df['COLUMN'].str.split('DELIMITER', n=1, expand=True)``` – Splits a column by a delimiter into multiple new columns.  

#### 🔗 Merging Columns
```df['NEW_COLUMN'] = df['COLUMN_1'] + 'SEPARATOR' + df['COLUMN_2']``` – Creates a new column by concatenating two columns with a separator.  

#### ✏️ Renaming and Formatting
```df.rename(columns={'OLD_NAME': 'NEW_NAME'}, inplace=True)``` – Renames a column.  
```df.columns = ['COLUMN_1', 'COLUMN_2', 'COLUMN_3', ...]``` – Sets new column names explicitly.

#### 🧵 Modifying Column Strings
```df.columns = [x.lower() for x in df.columns]``` – Converts all column names to lowercase.  
```df.columns = df.columns.str.replace(" ", "_")``` – Replaces spaces with underscores in column names.  
```df['COLUMN'] = df['COLUMN'].str.upper()``` – Converts all values in a column to uppercase.  

#### 🧠 Applying Custom Functions
```df['COLUMN'] = df['COLUMN'].apply(str.lower)``` – Applies the lowercase function to all entries in a column.   
```df['COLUMN'] = df['COLUMN'].apply(custom_function)``` – Applies a custom function to a column.  
```df['COLUMN'] = df['COLUMN'].apply(lambda x: x.lower())``` – Applies a lambda function to convert strings to lowercase.  
```df['COLUMN'] = df['COLUMN'].replace({'OLD_VALUE': 'NEW_VALUE'})``` – Replaces specific values in a column according to a mapping.  
```df['COLUMN'] = df['COLUMN'].map({'OLD_VALUE': 'NEW_VALUE'})``` – Maps old values to new values in a column.

#### 🎯 Conditional Modifications
```filter = df['COLUMN'] == 'VALUE'``` – Creates a boolean mask for rows where a column equals a value.  
```df.loc[filter, 'COLUMN_TO_MODIFY'] = 'NEW_VALUE'``` – Updates values in a column based on the condition.  
```df['COLUMN'] = df['COLUMN'].where(df['COLUMN'] < VALUE, other=np.nan)``` – Sets values to `NaN` where a condition is not met.  
```df['COLUMN'] = df['COLUMN'].clip(lower=LOWER_BOUND, upper=UPPER_BOUND)``` – Restricts values in a column to a specified range.

#### ✍️ Modifying by Index or Label
```df.loc[INDEX] = ['VALUE_1', 'VALUE_2', ...]``` – Replaces all column values in a row at a specific index.  
```df.loc[INDEX, 'COLUMN'] = VALUE``` – Updates a single cell value by index and column label.  
```df.loc[INDEX, ['COLUMN_1', 'COLUMN_2']] = [VALUE_1, VALUE_2]``` – Updates multiple columns in a row by index.  
```df.at[INDEX, 'COLUMN'] = VALUE``` – Assigns a single value to a specific cell identified by label-based index and column.

👉 Check out more in the [Jupyter notebook](notebooks/06-data-modifying.ipynb) or [Python Script](src/06_data_modifying.py).

---
### 07 Data Combining
Explains how to concatenate, merge, and join multiple datasets using pandas’ flexible tools.  

#### 🔀 Concatenation
```pd.concat([df1, df2])``` – Concatenates two DataFrames vertically (row-wise).  
```pd.concat([df1, df2], axis=1)``` – Concatenates two DataFrames horizontally (column-wise).  

#### 🔗 Merging
```pd.merge(df, new_df, on='INDEX_COLUMN')``` – Merges the original and new DataFrame on a shared index column.  

#### 🔄 Join Types: ```inner```, ```outer```, ```left```, ```right```
```pd.merge(left_df, right_df, on='INDEX_COLUMN', how='inner')``` – Performs an inner merge, keeping only matching index values.  
```pd.merge(left_df, right_df, on='INDEX_COLUMN', how='outer')``` – Performs an outer merge, keeping all index values from both DataFrames.  
```pd.merge(left_df, right_df, on='INDEX_COLUMN', how='left')``` – Performs a left join, keeping all index values from the left DataFrame.  
```pd.merge(left_df, right_df, on='INDEX_COLUMN', how='right')``` – Performs a right join, keeping all index values from the right DataFrame.  

#### 🧩 Joining
```df.join(df_new, on='INDEX_COLUMN')``` – Joins the new DataFrame to the original using their shared index.  

👉 Check out more in the [Jupyter notebook](notebooks/07-data-combining.ipynb) or [Python Script](src/07_data_combining.py).

---
### 08 Data Analyzing
Walks through filtering, sorting, grouping, aggregating, and pivoting data for insightful analysis.  

#### 🔍 Filtering data
```df['COLUMN'] == VALUE``` – Creates a filter for rows where the column equals a specific value.  
```df.loc[FILTER, ['COLUMN_1', 'COLUMN_2']]``` – Filters rows based on a filter and selects specific columns.  

#### 🔽 Sorting data
```df['COLUMN'].sort_values()``` – Returns a Series sorted by values in ascending order.  
```df.sort_values(by=['COLUMN_1', 'COLUMN_2'], ascending=[True, False])``` – Sorts the DataFrame by multiple columns with specified sort orders.  
```df['COLUMN'].nlargest(N)``` – Returns the N largest values in a column.  
```df.nlargest(N, 'COLUMN')``` – Returns the N rows with the largest values in a column.  
```df.nsmallest(N, 'COLUMN')``` – Returns the N rows with the smallest values in a column.  

#### 🧮 Aggregating  data
```df['COLUMN'].mean()``` – Calculates the mean of a column.  
```df['COLUMN'].median()``` – Calculates the median of a column.  
```df['COLUMN'].mode()``` – Returns the mode(s) of a column.  
```df[['COLUMN_1', 'COLUMN_2']].corr()``` – Computes the pairwise correlation between columns.  
```df[['COLUMN_1', 'COLUMN_2']].cov()``` – Computes the pairwise covariance between columns.

#### 👥 Grouping data
```df.groupby(['COLUMN'])['COLUMN_2'].mean()``` – Groups the DataFrame by one column and calculates the mean of another.  
```df.groupby(['COLUMN_1', 'COLUMN_2'])``` – Creates a multi-level groupby object.  
```group['COLUMN'].value_counts()``` – Counts unique values in each group.  
```group['COLUMN'].value_counts().loc[KEY]``` – Returns value counts for a specific group key.  
```group['COLUMN'].value_counts(normalize=True)``` – Calculates the relative frequencies of values in each group.  
```group['COLUMN'].median()``` – Computes the median for each group.  
```group['COLUMN'].median().loc[KEY]``` – Retrieves the median for a specific group key.  
```group['COLUMN'].agg(['median', 'mean', 'std', 'min', 'max'])``` – Aggregates multiple statistics per group.  
```group['COLUMN'].agg(['median', 'mean']).loc[KEY]``` – Aggregates selected stats and selects a specific group.  
```group['COLUMN'].apply(lambda x: x.str.contains('PATTERN').sum())``` – Counts how many entries in each group match a string pattern.  
```df['COLUMN'].value_counts()``` – Counts unique values in a column.  
```df['COLUMN'].count()``` – Counts non-null values in a column.  
```group['COLUMN'].apply(lambda x: x.str.contains('PATTERN').sum()).loc[KEY]``` – Retrieves counts for a pattern-matching condition from a specific group.  
```group['COLUMN'].count()``` – Counts non-null entries in a column for each group.  
```df.groupby('COLUMN').agg({'COLUMN_1': ['mean', 'median'], 'COLUMN_2': ['mean', 'max', 'min']})``` – Applies multiple aggregation functions on multiple columns grouped by a specified column.  

#### 📊 Pivoting data
```df.pivot(index='COLUMN', columns='COLUMN_2', values=['COLUMN_3'])``` – Reshapes the DataFrame based on column values as new columns.  
```pd.pivot_table(df, index='COLUMN_1', columns='COLUMN_2', values='COLUMN_3', aggfunc='mean')``` – Creates a pivot table using the mean as the aggregation function.  
```pd.pivot_table(df, index='COLUMN_1', columns='COLUMN_2', values=['COLUMN_3', 'COLUMN_4'], aggfunc=['mean', 'median'])``` – Creates a pivot table with multiple values and aggregation functions.  

👉 Check out more in the [Jupyter notebook](notebooks/08-data-analyzing.ipynb) or [Python Script](src/08_data_analyzing.py).

---
### 09 Dates & Time Series
Introduces handling of datetime data, time series analysis, and date-based operations in pandas.  

#### 📅 Datetime Conversion
```pd.read_csv(PATH, parse_dates=['COLUMN'], date_format='FORMAT')``` – Reads CSV and parses specified column as datetime.  
```pd.to_datetime(df['COLUMN'], format='FORMAT')``` – Converts string-formatted date column to datetime.  

#### 🕰️ Creating Date Ranges
```pd.date_range(START_DATE, periods=NUM, freq='FREQ')``` – Generates a sequence of dates with a specified frequency.  
```pd.DataFrame(data=SEQUENCE, columns=['COLUMN'])``` – Creates a DataFrame from a date sequence.  

#### 🕓 Accessing Time Components
```df.at_time('HH:MM')``` – Filters data for a specific time of day.  
```df.between_time('START', 'END')``` – Filters data between two times of day.

#### 🕓 Accessing Time with .dt
```df['COLUMN'].dt.year``` – Extracts the year from datetime.  
```df['COLUMN'].dt.month``` – Extracts the month from datetime.  
```df['COLUMN'].dt.quarter``` – Extracts the quarter of the year.  
```df['COLUMN'].dt.day``` – Extracts the day of the month.  
```df['COLUMN'].dt.hour``` – Extracts the hour.  
```df['COLUMN'].dt.minute``` – Extracts the minute.  
```df['COLUMN'].dt.second``` – Extracts the second.  
```df['COLUMN'].dt.day_name()``` – Gets the day name (e.g., Monday).

#### 🕓 Accessing Date Properties
```df.loc[ROW, 'COLUMN'].date()``` – Extracts date part (no time).  
```df.loc[ROW, 'COLUMN'].day_name()``` – Gets name of the weekday.  
```df.loc[ROW, 'COLUMN'].month_name()``` – Gets name of the month.  
```df.loc[ROW, 'COLUMN'].day``` – Extracts day.  
```df.loc[ROW, 'COLUMN'].week``` – Extracts week number of the year.  
```df.loc[ROW, 'COLUMN'].dayofweek``` – Extracts day of week as integer.  
```df.loc[ROW, 'COLUMN'].month``` – Extracts numeric month.  
```df.loc[ROW, 'COLUMN'].year``` – Extracts year.

#### 🕓 Time Differences with Timedelta
```df['COLUMN'].min()``` – Finds earliest datetime.  
```df['COLUMN'].max()``` – Finds latest datetime.  
```df['COLUMN'].max() - df['COLUMN'].min()``` – Computes timedelta between two dates.

### 📆 Working with Period and Offsets
```pd.Period('VALUE')``` – Creates a period object (e.g., year, month).  
```period.start_time``` – Returns start time of the period.  
```period.end_time``` – Returns end time of the period.  
```period += pd.offsets.FREQ(AMOUNT)``` – Offsets a period forward or backward in time.  

#### 🌍 Timezones and Localization
```df['COLUMN'].dt.tz_localize('TIMEZONE')``` – Localizes datetime column to a timezone.  
```df['COLUMN'].dt.tz_convert('TIMEZONE')``` – Converts timezone of a datetime column.

#### 🔍 Filtering and Slicing Dates
```df['COLUMN'] > pd.to_datetime('DATE')``` – Filters rows on a datetime condition.  
```df.index > pd.Timestamp('DATE')``` – Filters rows on a Timestamp condition.  
```df.loc['YEAR']``` – Slices all rows for a specific year.  
```df.loc['START_DATE' : 'END_DATE']``` – Slices rows between two dates.

#### 📊 Frequency Conversion, Resampling and Rolling
```df.asfreq('FREQ')``` – Changes frequency without aggregation.  
```df.resample('FREQ')['COLUMN'].mean()``` – Resamples data and calculates mean.  
```df['COLUMN'].rolling(window=N).mean()``` – Computes rolling mean over a window.

#### 🔧 Handling Missing Data with .interpolate()
```df['COLUMN'].interpolate(limit_direction='both')``` – Fills missing values using interpolation.

#### 📈 Calculating Lagged Values and Differences
```df['COLUMN'].shift(N)``` – Shifts values by N periods (e.g., previous day's value).  
```df['COLUMN'].diff()``` – Calculates the difference between current and previous value.  
```df['COLUMN'].pct_change()``` – Calculates percentage change from previous value.

👉 Check out more in the [Jupyter notebook](notebooks/09-dates-timeseries.ipynb) or [Python Script](src/09_dates_timeseries.py).

---
### 10 Plotting & Visualization
Demonstrates how to create common visualizations such as line plots, bar charts, histograms, and scatter plots to explore and communicate data insights effectively.  

#### 📈 Basic Plotting Functions
```df.plot(subplots=True, title='TITLE')``` – Plots each numeric column in a separate subplot with a title.  
```df.plot(kind='line', title='TITLE')``` – Plots all columns as line charts with a title.  
```df[['COLUMN_1', 'COLUMN_2']].plot(kind='line', title='TITLE')``` – Plots two columns as separate lines on the same plot.  
```df.plot(kind='scatter', x='COLUMN_X', y='COLUMN_Y', title='TITLE')``` – Creates a scatter plot between two variables.  
```df.plot(kind='hexbin', x='COLUMN_X', y='COLUMN_Y', title='TITLE')``` – Creates a hexbin density plot for two variables.  
```df[['COLUMN_1', 'COLUMN_2']].plot(stacked=True, title='TITLE')``` – Plots multiple columns as a stacked area chart.  
```df['COLUMN'].plot(kind='line', title='TITLE')``` – Creates a line chart of a single column.  
```df['COLUMN'].plot(kind='area', title='TITLE')``` – Creates an area chart of a single column.  
```df['COLUMN'].plot(kind='bar', title='TITLE')``` – Creates a bar chart of a single column.  
```df['COLUMN'].plot(kind='hist', bins=N, title='TITLE')``` – Creates a histogram with N bins.  
```df['COLUMN'].plot(kind='box', title='TITLE')``` – Creates a box plot for a single column.  
```df['COLUMN'].value_counts().plot(kind='pie', title='TITLE')``` – Creates a pie chart from value counts of a column.

#### 🎨 Basic Customizations
```df[['COLUMN_1', 'COLUMN_2']].plot(kind='KIND', title='TITLE', xlabel='LABEL', ylabel='LABEL', color=['COLOR_1', 'COLOR_2'], figsize=(WIDTH, HEIGHT), grid=True, legend=True, alpha=VALUE)``` – Creates a customized line chart with labels, size, grid, colors, and transparency.

#### 🔧 Plot Configuration
```df['COLUMN'].plot(title='TITLE', figsize=(WIDTH, HEIGHT), style='STYLE', color='COLOR', linewidth=VALUE, alpha=VALUE, xlim=('START', 'END'), ylim=(LOW, HIGH), rot=ANGLE)``` – Creates a styled line plot with axis limits, rotation, and transparency.  
```axis2 = df['COLUMN_2'].plot(ax=axis1, secondary_y=True, ...)``` – Overlays a second line with a secondary y-axis.   
```axis2.set_ylabel('LABEL')``` – Sets y-axis label for the secondary axis.   
```axis1.set_ylabel('LABEL')``` – Sets y-axis label for the primary axis.   
```axis1.legend(['LABEL'], loc='LOCATION')``` – Adds a legend for the first plot.   
```axis1.right_ax.legend(['LABEL'], loc='LOCATION')``` – Adds a legend for the second axis.   
```plt.show()``` – Displays the plot.  

#### 🖼️ Save Plots
```plt.savefig(export_path)``` – Saves the current plot to the specified file path.

👉 Check out more in the [Jupyter notebook](notebooks/10-plotting-visualization.ipynb) or [Python Script](src/10_plotting_visualization.py).


---

## Who this is for
- **Beginners** who want to learn pandas from scratch.
- **Students** in data science, machine learning, or analytics.
- **Anyone** who prefers learning by example and hands-on code.

---

## Datasets used
- [Ramen Ratings](https://www.kaggle.com/datasets/residentmario/ramen-ratings/data)
- [Titanic: Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data)
- [Weather Prediction](https://www.kaggle.com/datasets/ananthr1/weather-prediction/data)

_Datasets should be placed in the appropriate `/data/raw/` or `/data/processed/` folders as described in each notebook._

---

## Contributing
Contributions to this project are welcome! If you would like to contribute, please open an issue to discuss potential changes or submit a pull request. 
For more details please visit the [contributing page](docs/CONTRIBUTING.md).

---

## License
This project is licensed under the [MIT License](LICENSE.md). You are free to use, modify, and distribute this code as permitted by the license.

---
 
<h4 align="center">
    Happy pandas coding! 🐼
</h4>

![Happy Pandas Coding](res/pandas-coding.png)

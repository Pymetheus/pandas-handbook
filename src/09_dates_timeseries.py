# --- Pandas Handbook: 09 - Dates and Time Series ---
# Demonstrates time-based operations using the Weather dataset


# --- Import Libraries ---
# Import pandas for data handling and os for path operations
import pandas as pd
import os


# --- Load Dataset ---
# Define the file path and load the weather dataset CSV into a DataFrame.
data_raw = "../data/raw/"
csv_file = "weather.csv"
import_path = os.path.join(data_raw, csv_file)

df = pd.read_csv(import_path)

# Show first 3 rows to inspect the data
print(df.head(3))


# --- Inspect Data Types ---
# Display the data types of the columns to check which columns require conversion.
print(df.dtypes)


# --- Datetime Conversion ---
# Load the CSV again with 'date' parsed as datetime (using parse_dates).
df = pd.read_csv(import_path, parse_dates=['date'], date_format='%Y-%m-%d')

# Show data types to confirm 'date' column is datetime
print(df.dtypes)

# Verify the type of the first date value
print(type(df.loc[0, 'date']))

# Alternatively, convert 'date' column to datetime after loading
df = pd.read_csv(import_path)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Show data types again to confirm conversion
print(df.dtypes)

# Verify type again after conversion
print(type(df.loc[0, 'date']))


# --- Creating Date Ranges ---
# Create a daily date range of 30 days starting from 1/1/2012 and put it in a DataFrame
time_range = pd.date_range('1/1/2012', periods=30, freq='d')
time_range_df = pd.DataFrame(data=time_range, columns=['date'])
time_range_df.set_index('date', inplace=True)

print(time_range_df.head())

# Create an hourly date range of 100 hours starting from 1/1/2012
time_range = pd.date_range('1/1/2012', periods=100, freq='h')
time_range_df = pd.DataFrame(data=time_range, columns=['date'])
time_range_df.set_index('date', inplace=True)

print(time_range_df.head())


# --- Accessing Time Components ---
# Filter the DataFrame for rows at exactly 09:00 hours
print(time_range_df.at_time('09:00'))

# Filter rows between 00:00 and 02:00 hours
print(time_range_df.between_time('00:00', '02:00'))


# --- Accessing Time with .dt accessor ---
# Extract year component from 'date' column
print(df['date'].dt.year)

# Extract month component
print(df['date'].dt.month)

# Extract quarter of the year
print(df['date'].dt.quarter)

# Extract day of the month
print(df['date'].dt.day)

# Extract hour component (will be zero since original data is date only)
print(df['date'].dt.hour)

# Extract minute component (zero here)
print(df['date'].dt.minute)

# Extract second component (zero here)
print(df['date'].dt.second)

# Get day name (e.g., Monday, Tuesday)
print(df['date'].dt.day_name())


# --- Accessing Date Properties of a Specific Row ---
# Show full Timestamp object of row index 8
print(df.loc[8, 'date'])

# Extract date part only (no time)
print(df.loc[8, 'date'].date())

# Get day name of the date at index 8
print(df.loc[8, 'date'].day_name())

# Get month name
print(df.loc[8, 'date'].month_name())

# Extract day of the month
print(df.loc[8, 'date'].day)

# Extract week number of the year (deprecated alias warning may appear)
print(df.loc[8, 'date'].week)

# Extract day of week as integer (Monday=0, Sunday=6)
print(df.loc[8, 'date'].dayofweek)

# Extract numeric month for first row
print(df.loc[0, 'date'].month)

# Extract year for first row
print(df.loc[0, 'date'].year)


# --- Time Differences with Timedelta ---
# Find earliest date in dataset
print(df['date'].min())

# Find latest date in dataset
print(df['date'].max())

# Compute timedelta between max and min date
timedelta = df['date'].max() - df['date'].min()
print(timedelta)


# --- Working with Periods and Offsets ---
# Create a period representing the year 2021
year = pd.Period('2021')

# Get start time of the period
print(year.start_time)

# Get end time of the period
print(year.end_time)

# Create periods of month, day, and hour frequency
month = pd.Period('2022-01')
day = pd.Period('2022-01', freq='d')
hour = pd.Period('2022-02-09 16:00:00', freq='h')

print(hour)

# Offset the hour period by +2 hours
hour += pd.offsets.Hour(+2)
print(hour)

# Generate a week range and print day of week and date for each day
week = pd.date_range('2022-2-7', periods=7)
for day in week:
    print(f'{day.day_of_week}-{day.day_name()}\t{day.date()}')


# --- Timezones and Localization ---
# Create a copy of the DataFrame and localize 'date' to UTC timezone
timezone_df = df.copy()
timezone_df['date_utc'] = timezone_df['date'].dt.tz_localize('UTC')

print(timezone_df['date_utc'].head())

# Convert UTC time to US/Pacific timezone
timezone_df['date_pacific'] = timezone_df['date_utc'].dt.tz_convert('US/Pacific')

print(timezone_df[['date_utc', 'date_pacific']].head())


# --- Filtering and Slicing Dates ---
# Filter rows where date is after year 2013
time_filter = (df['date'] > pd.to_datetime('2013'))
print(df.loc[time_filter].head(3))

# Set 'date' as index and sort to enable slicing by date range
filter_df = df.copy()
filter_df.set_index('date', inplace=True)
filter_df.sort_index(inplace=True)

# Filter rows between 2013-01-02 and 2013-01-07
period_filter = (filter_df.index >= pd.Timestamp('2013-01-02')) & (filter_df.index < pd.Timestamp('2013-01-07'))
print(filter_df.loc[period_filter].head(3))

# Slice all rows for year 2013
slice_df = df.copy()
slice_df.set_index('date', inplace=True)
slice_df.sort_index(inplace=True)

print(slice_df.loc['2013'].head(3))

# Slice rows between two specific dates
print(slice_df.loc['2013-01-02':'2013-01-09'])


# --- Frequency Conversion, Resampling and Rolling ---
# Set 'date' as index for resampling operations
weekly_df = df.copy()
weekly_df.set_index('date', inplace=True)
weekly_df.sort_index(inplace=True)

# Change frequency to weekly without aggregation
print(weekly_df.asfreq('W').head(3))

# Resample monthly end ('ME') and calculate mean of temp_max
resample_df = df.copy()
resample_df.set_index('date', inplace=True)
resample_df.sort_index(inplace=True)

monthly_temp = resample_df.resample('ME')['temp_max'].mean()
print(monthly_temp.head(3))

# Resample yearly end ('YE') and calculate mean of temp_min
monthly_temp = resample_df.resample('YE')['temp_min'].mean()
print(monthly_temp.head(3))

# Calculate rolling mean with a window size of 3 for temp_max
rolling_df = df.copy()
rolling_df.set_index('date', inplace=True)
rolling_df.sort_index(inplace=True)

rolling_df['temp_max'] = rolling_df['temp_max'].rolling(window=3).mean()
print(rolling_df['temp_max'].head())


# --- Handling Missing Data with .interpolate() ---
# Check how many missing values are present in 'temp_max' after rolling mean
interpolate_df = rolling_df.copy()
print(interpolate_df['temp_max'].isna().sum())

# Interpolate missing values in 'temp_max' column
interpolate_df['temp_max'] = interpolate_df['temp_max'].interpolate(limit_direction='both')
print(interpolate_df.head())


# --- Calculating Lagged Values and Differences ---
# Shift temp_max values by 1 period to get previous day's value
shift_df = df.copy()
shift_df.set_index('date', inplace=True)
shift_df.sort_index(inplace=True)

shift_df['temp_max_prev_day'] = shift_df['temp_max'].shift(1)
print(shift_df[['temp_max', 'temp_max_prev_day']].head(3))

# Calculate difference between current and previous temp_max
diff_df = df.copy()
diff_df.set_index('date', inplace=True)
diff_df.sort_index(inplace=True)

diff_df['temp_max_diff'] = diff_df['temp_max'].diff()
print(diff_df[['temp_max', 'temp_max_diff']].head(3))

# Calculate percentage change of temp_max from previous value
pctchange_df = df.copy()
pctchange_df.set_index('date', inplace=True)
pctchange_df.sort_index(inplace=True)

pctchange_df['temp_max_diff_pct'] = pctchange_df['temp_max'].pct_change()
print(pctchange_df[['temp_max', 'temp_max_diff_pct']].head(3))


# --- Footer ---
"""
🐼 Pandas Handbook by Pymetheus

🔗 Official Pandas documentation:
https://pandas.pydata.org/pandas-docs/stable/

📘 Explore the interactive set of jupyter notebooks:
https://github.com/Pymetheus/pandas-handbook/notebooks

🔗 Explore the Weather Dataset:
https://www.kaggle.com/datasets/ananthr1/weather-prediction/data
"""

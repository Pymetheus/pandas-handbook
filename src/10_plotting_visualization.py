# --- Pandas Handbook: 10 - Plotting & Visualization ---
# This script demonstrates how to visualize data in pandas using a weather dataset.


# --- Import Libraries ---
# Import pandas for data handling, matplotlib for visualization and os for path operations
import pandas as pd
import matplotlib.pyplot as plt
import os


# --- Load Dataset ---
# Load the weather dataset, parse dates and set the 'date' column as the index.
data_raw = "../data/raw/"
csv_file = "weather.csv"
import_path = os.path.join(data_raw, csv_file)
df = pd.read_csv(import_path, parse_dates=['date'], date_format='%Y-%m-%d')
df.set_index('date', inplace=True)

# Show first 3 rows of the dataframe
print(df.head(3))


# --- Basic Plotting Functions ---
# Plot each numeric column in a separate subplot with a title.
print("Plotting all weather conditions with subplots...")
ax = df.plot(subplots=True, title='Weather conditions')
plt.show()

# Filter dataframe for January 2012
jan_df = df.loc['2012-01-01' : '2012-01-31']

# Line plot of all columns in January
print("Plotting weather conditions in January...")
ax = jan_df.plot(kind='line', title='Weather conditions in January')
plt.show()

# Line plot comparing max and min temperature in January
print("Plotting max vs min temperature in January...")
ax = jan_df[['temp_max', 'temp_min']].plot(kind='line', title='Max. vs min. temperature')
plt.show()

# Scatter plot of min vs max temperature in January
print("Plotting scatter plot of temperature distribution...")
ax = jan_df.plot(kind='scatter', x='temp_min', y='temp_max', title='Temperature Distribution')
plt.show()

# Hexbin density plot of min vs max temperature in January
print("Plotting hexbin density plot of temperature distribution...")
ax = jan_df.plot(kind='hexbin', x='temp_min', y='temp_max', title='Temperature Distribution')
plt.show()

# Stacked area plot for wind and precipitation in January
print("Plotting stacked area chart for wind and precipitation...")
ax = jan_df[['wind', 'precipitation']].plot(stacked=True, title='Wind & Precipitation Distribution')
plt.show()

# Line plot of wind over time in January
print("Plotting wind over time (line)...")
ax = jan_df['wind'].plot(kind='line', title='Wind over Time')
plt.show()

# Area plot of wind over time in January
print("Plotting wind over time (area)...")
ax = jan_df['wind'].plot(kind='area', title='Wind over Time')
plt.show()

# Bar plot of wind over time in January
print("Plotting wind over time (bar)...")
ax = jan_df['wind'].plot(kind='bar', title='Wind over Time')
plt.show()

# Histogram of wind strength distribution in January
print("Plotting histogram of wind strength...")
ax = jan_df['wind'].plot(kind='hist', bins=10, title='Wind over Time')
plt.show()

# Box plot of wind distribution in January
print("Plotting box plot of wind strength...")
ax = jan_df['wind'].plot(kind='box', title='Wind Box Plot')
plt.show()

# Pie chart of wind strength distribution in January
print("Plotting pie chart of wind strength distribution...")
ax = jan_df['wind'].value_counts().plot(kind='pie', title='Wind Strength Distribution')
plt.show()


# --- Basic Customizations ---
# Customized line chart for temperature change in January with colors, grid, and transparency.
print("Plotting customized temperature line chart...")
jan_df[['temp_max', 'temp_min']].plot(
    kind='line',
    title='Change in Temperature over Time',
    xlabel='Time',
    ylabel='Temperature',
    color=['red', 'blue'],
    figsize=(12, 6),
    grid=True,
    legend=True,
    alpha=0.4
)
plt.show()


# --- Plot Configuration ---
# Styled line plot of max temperature with axis limits, line style, color, and rotation.
print("Plotting max temperature with custom style and axis limits...")
max_temp_axis = df['temp_max'].plot(
    title='Max Temperature',
    figsize=(12, 6),
    style='--o',
    color='red',
    linewidth=2,
    alpha=0.8,
    xlim=('2012-01', '2012-03'),
    ylim=(0, 25),
    rot=45,
)
plt.show()

# Overlay plot with max temperature and wind speed using secondary y-axis.
print("Plotting max temperature with wind speed overlay...")
max_temp_axis = df['temp_max'].plot(
    title='Max Temperature with Wind Speed Overlay',
    figsize=(12, 6),
    style='--o',
    color='red',
    linewidth=2,
    alpha=0.8,
    xlim=('2012-01', '2012-03'),
    ylim=(0, 25),
    rot=45
)

wind_axis = df['wind'].plot(
    ax=max_temp_axis,
    secondary_y=True,
    style='-s',
    color='steelblue',
    linewidth=1.5,
    alpha=0.6,
    xlim=('2012-01', '2012-03'),
    ylim=(0, 10),
    rot=45,
    label='Wind Speed'
)

# Set axis labels and legends
wind_axis.set_ylabel('Wind (km/h)')
max_temp_axis.set_ylabel('Celsius (°C)')
max_temp_axis.legend(['Max Temp'], loc='upper left')
max_temp_axis.right_ax.legend(['Wind Speed'], loc='upper right')

# Display the combined plot
plt.show()


# --- Save Plots ---
# Define path to save plot image
data_processed = "../data/processed/"
png_file = "test_file.png"
export_path = os.path.join(data_processed, png_file)

# Plot all weather conditions and save the figure
print("Plotting weather conditions and saving figure...")
df.plot(subplots=True, title='Weather conditions')
plt.savefig(export_path)
print(f"Plot saved to {export_path}")
plt.close()


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

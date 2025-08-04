# --- Pandas Handbook: 08 - Data Analyzing - Filtering, Sorting, Grouping, Aggregating & Pivoting ---
# Demonstrates data analyzing techniques using the Titanic dataset


# --- Import Libraries ---
# Import pandas for data handling and os for path operations
import pandas as pd
import os


# --- Load Dataset ---
# Define file path and load the Titanic dataset with PassengerId as index
data_processed = "../data/processed/"
csv_file = "clean_titanic.csv"
import_path = os.path.join(data_processed, csv_file)
df = pd.read_csv(import_path, index_col="PassengerId")

print(df.head(3))


# --- Filtering Data ---
# Create a filter for third-class survivors (Survived=1 and Pclass=3)
third_class_survivers_filter = ((df['Survived'] == 1) & (df['Pclass'] == 3))

# Apply the filter and select specific columns
third_class_survivers_df = df.loc[third_class_survivers_filter, ['Name', 'Sex', 'Age', 'Fare']]

print(third_class_survivers_df.head(3))

# Display the number of third-class survivors
print(len(third_class_survivers_df))


# --- Sorting Data ---
# Sort the 'Age' column of the filtered DataFrame in ascending order
print(third_class_survivers_df['Age'].sort_values())

# Sort the DataFrame by 'Age' ascending and 'Fare' descending
third_class_survivers_df = third_class_survivers_df.sort_values(by=['Age', 'Fare'], ascending=[True, False])

print(third_class_survivers_df.head())

# Display the 5 largest values in the 'Age' column
print(third_class_survivers_df['Age'].nlargest(5))

# Display the 5 rows with the largest 'Fare' values
print(third_class_survivers_df.nlargest(5, 'Fare'))

# Display the 5 rows with the smallest 'Fare' values
print(third_class_survivers_df.nsmallest(5, 'Fare'))


# --- Aggregating Data ---
# Calculate and print the mean age of third-class survivors
print(third_class_survivers_df['Age'].mean())

# Calculate and print the median age of third-class survivors
print(third_class_survivers_df['Age'].median())

# Calculate and print the mode(s) of the age column for third-class survivors
print(third_class_survivers_df['Age'].mode())

# Compute and print the correlation matrix for selected columns
correlation_matrix = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].corr()
print(correlation_matrix)

# Compute and print the covariance matrix for selected columns
covariance_matrix = df[['Survived', 'Age', 'Fare']].cov()
print(covariance_matrix)


# --- Grouping Data ---
# Group the DataFrame by 'Survived' and calculate mean age for each group
new_group = df.groupby(['Survived'])['Age'].mean()
print(new_group)

# Create a multi-level groupby object grouped by 'Survived' and 'Pclass'
new_group = df.groupby(['Survived', 'Pclass'])

# Get the group for Survived=1 and Pclass=1
print(new_group.get_group((1, 1)))

# Calculate value counts of 'Sex' within each group of the multi-level grouping
print(new_group['Sex'].value_counts())

# Value counts of 'Sex' for Survived=1
print(new_group['Sex'].value_counts().loc[1])

# Calculate normalized value counts (proportions) of 'Sex' in each group
print(new_group['Sex'].value_counts(normalize=True))

# Calculate median age per group
print(new_group['Age'].median())

# Median age for Survived=0 group by Pclass
print(new_group['Age'].median().loc[0])

# Aggregate multiple statistics on 'Age' per group
print(new_group['Age'].agg(['median', 'mean', 'std', 'min', 'max']))

# Aggregate median and mean of 'Age' for Survived=0 group
print(new_group['Age'].agg(['median', 'mean']).loc[0])

# Count how many entries in each group have 'Mrs.' in their 'Name'
print(new_group['Name'].apply(lambda x: x.str.contains('Mrs.').sum()))

# Count 'Mrs.' occurrences for Survived=0 group
print(new_group['Name'].apply(lambda x: x.str.contains('Mrs.').sum()).loc[0])

# Count unique values in 'Survived' column
print(df['Survived'].value_counts())

# Count non-null entries in 'Survived' column
print(df['Survived'].count())

# Repeat count of 'Mrs.' occurrences (same as before, for clarity)
print(new_group['Name'].apply(lambda x: x.str.contains('Mrs.').sum()))

# Combine total passengers and Mrs. counts into a new DataFrame
total_passengers = new_group['Name'].count()
mrs_count = new_group['Name'].apply(lambda x: x.str.contains('Mrs.').sum())
new_df = pd.concat([total_passengers, mrs_count], axis=1)
new_df.columns = ['Total', 'Mrs_Count']

print(new_df)

# Aggregate mean and median of 'Age' and mean, max, min of 'Fare' grouped by 'Pclass'
agg_df = df.groupby('Pclass').agg({
    'Age': ['mean', 'median'],
    'Fare': ['mean', 'max', 'min']
})
print(agg_df)


# --- Pivoting Data ---
# Create a pivot table indexed by 'Name', with columns by 'Sex' and values from 'Age'
pivoted_df = df.pivot(index='Name', columns='Sex', values=['Age'])
print(pivoted_df.head(3))

# Create a pivot table indexed by 'Sex' and columns by 'Pclass', aggregating mean 'Fare'
pivot = pd.pivot_table(df, index='Sex', columns='Pclass', values='Fare', aggfunc='mean')
print(pivot)

# Create a pivot table indexed by 'Sex' and columns by 'Pclass', aggregating mean and median of 'Survived' and 'Age'
pivot = pd.pivot_table(df, index='Sex', columns='Pclass', values=['Survived', 'Age'], aggfunc=['mean', 'median'])
print(pivot)


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

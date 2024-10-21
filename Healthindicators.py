
import pandas as pd

# Load the Excel file using a raw string for the file path
file_path = r'C:\Users\ADMIN\Desktop\P1\data\physician-density-in-kenya-xlsx-2.xlsx'
df = pd.read_excel(file_path)

# Display the first few rows to understand the structure
print(df.head())

# Rename columns for clarity
df.columns = ['Country', 'County', 'Physicians Density']

# Drop any rows that might not be relevant (e.g., header rows that were imported as data)
df = df.dropna(subset=['Physicians Density'])

# Display the cleaned data
print(df.head())


# Remove the row where 'Country' is "COUNTRY"
df = df[df['Country'] != 'COUNTRY']

# Convert 'Physicians Density' to numeric for analysis
df['Physicians Density'] = pd.to_numeric(df['Physicians Density'], errors='coerce')

# Display the cleaned data
print(df.head())


# Basic statistics for Physicians Density


import pandas as pd

# Load the Excel file
file_path = r'C:\Users\ADMIN\Desktop\P1\data\physician-density-in-kenya-xlsx-2.xlsx'
df = pd.read_excel(file_path)

 #Rename columns for clarity
df.columns = ['Country', 'County', 'Physicians Density']

# Print the column names
print(df.columns)

df['Physicians Density'] = pd.to_numeric(df['Physicians Density'], errors='coerce')

summary_stats = df['Physicians Density'].describe()
print(summary_stats)


# Top 5 counties with the highest physician density
top_5_counties = df.sort_values(by='Physicians Density', ascending=False).head(5)

# Bottom 5 counties with the lowest physician density
bottom_5_counties = df.sort_values(by='Physicians Density').head(5)

print("Top 5 Counties with the Highest Physician Density:\n", top_5_counties)
print("\nBottom 5 Counties with the Lowest Physician Density:\n", bottom_5_counties)

# Extract the national average
national_average = df[df['County'] == 'National Average']['Physicians Density'].values[0]

# Counties with densities above the national average
above_average = df[df['Physicians Density'] > national_average]

# Counties with densities below the national average
below_average = df[df['Physicians Density'] < national_average]

print(f"National Average: {national_average}")
print(f"Counties above the national average: {above_average['County'].tolist()}")
print(f"Counties below the national average: {below_average['County'].tolist()}")

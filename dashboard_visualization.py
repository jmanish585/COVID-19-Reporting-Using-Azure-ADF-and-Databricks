# Notebook: dashboard_visualization.ipynb
# Purpose: Visualize COVID-19 hospitalization trends using data from Azure SQL DB

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pyodbc

# SQL Server connection settings
server = '<your_server>.database.windows.net'
database = '<your_database>'
username = '<your_username>'
password = '<your_password>'
driver = '{ODBC Driver 17 for SQL Server}'

# Connect to Azure SQL Database
conn_str = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
conn = pyodbc.connect(conn_str)

# Load aggregated data
df = pd.read_sql("SELECT Location, Year, Month, Monthly_Admissions, Monthly_Cases FROM CovidMonthlyReport", conn)

# Close connection
conn.close()

# Convert year/month to datetime for plotting
df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

# Sort values for proper timeline display
df = df.sort_values(by=['Location', 'Date'])

# Plot hospital admissions over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Date', y='Monthly_Admissions', hue='Location')
plt.title('Monthly COVID-19 Hospital Admissions by Country')
plt.xlabel('Date')
plt.ylabel('Hospital Admissions')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(True)
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset and convert the 'date' column to datetime format so we can work with it properly.
df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

# Print basic details to understand what kind of data we are working with.
print(df.head())
print("\nColumn Names:")
print(df.columns)
print("\nMissing Values:")
print(df.isnull().sum())

# Show some basic stats like mean, min, max, etc.
print("\nDescriptive Statistics:")
print(df.describe())

# Display how many unique companies are there and show a few sample names.
print(f"\nTotal unique companies: {df['symbol'].nunique()}")
print("Sample Ticker Symbols:", df['symbol'].unique()[:5])

# Get the Apple (AAPL) data separately for time-series plotting.
sample = df[df['symbol'] == 'AAPL']

# Find the top 5 most frequent companies in the dataset for comparison in volume.
top5 = df['symbol'].value_counts().head(5).index
top_df = df[df['symbol'].isin(top5)]

# Now we’ll create a single figure with 3 plots – Apple stock price trend, closing price distribution, and volume comparison of top 5 companies.
plt.figure(figsize=(16, 12))

# Plot 1 – Apple Stock Price Over Time
plt.subplot(3, 1, 1)
plt.plot(sample['date'], sample['close'], color='blue')
plt.title("Apple Stock Price Over Time (2014–2017)")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.grid(True)

# Plot 2 – Closing Price Distribution
plt.subplot(3, 1, 2)
sns.histplot(df['close'], bins=100, kde=True, color='green')
plt.title("Distribution of Closing Prices (All Companies)")
plt.xlabel("Close Price")
plt.ylabel("Frequency")

# Plot 3 – Volume Comparison of Top 5 Companies
plt.subplot(3, 1, 3)
sns.boxplot(x='symbol', y='volume', hue='symbol', data=top_df, palette="Set2", legend=False)
plt.title("Volume Traded by Top 5 Companies")
plt.ylabel("Volume")
plt.xlabel("Company")

# Adjust the layout so nothing overlaps
plt.tight_layout()
plt.show()

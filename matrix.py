import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

# Get top 10 most frequent companies
top_symbols = df['symbol'].value_counts().head(10).index.tolist()

# Filter only those companies
filtered_df = df[df['symbol'].isin(top_symbols)]

# Pivot data so each symbol becomes a column
pivot_df = filtered_df.pivot(index='date', columns='symbol', values='close')

# Drop dates with any missing values
pivot_df.dropna(inplace=True)

# Compute correlation
corr = pivot_df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation of Closing Prices (Top 10 Companies)")
plt.tight_layout()
plt.show()

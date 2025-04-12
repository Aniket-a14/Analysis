import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])


top_symbols = df['symbol'].value_counts().head(10).index.tolist()


filtered_df = df[df['symbol'].isin(top_symbols)]
pivot_df = filtered_df.pivot(index='date', columns='symbol', values='close')
pivot_df.dropna(inplace=True)
corr = pivot_df.corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation of Closing Prices (Top 10 Companies)")
plt.tight_layout()
plt.show()

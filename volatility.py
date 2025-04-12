import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

# We calculate standard deviation of closing price for each company and pick the top 10 most volatile ones
volatility_df = df.groupby('symbol')['close'].std().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=volatility_df.index, y=volatility_df.values, palette="Set1")
plt.title("Top 10 Most Volatile Stocks (2014–2017)")
plt.xlabel("Company Symbol")
plt.ylabel("Price Standard Deviation")
plt.tight_layout()
plt.show()

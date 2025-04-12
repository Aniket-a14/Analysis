import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

# We calculate percentage change from first to last closing price for each company
price_change = df.sort_values('date').groupby('symbol')['close'].agg(['first', 'last'])
price_change['percent_change'] = ((price_change['last'] - price_change['first']) / price_change['first']) * 100

# Top 10 gainers
top_gainers = price_change.sort_values('percent_change', ascending=False).head(10)
# Top 10 losers
top_losers = price_change.sort_values('percent_change').head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_gainers.index, y=top_gainers['percent_change'], palette="Greens")
plt.title("Top 10 Gainers (2014–2017)")
plt.ylabel("Percentage Gain")
plt.xlabel("Company Symbol")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x=top_losers.index, y=top_losers['percent_change'], palette="Reds")
plt.title("Top 10 Losers (2014–2017)")
plt.ylabel("Percentage Loss")
plt.xlabel("Company Symbol")
plt.tight_layout()
plt.show()

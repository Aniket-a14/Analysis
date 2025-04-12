import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

df['year'] = df['date'].dt.year
selected_symbols = ['AAPL', 'MSFT', 'AMZN', 'GOOG', 'TSLA']
filtered_df = df[df['symbol'].isin(selected_symbols)]


avg_yearly_price = filtered_df.groupby(['year', 'symbol'])['close'].mean().reset_index()

plt.figure(figsize=(14,7))
sns.lineplot(data=avg_yearly_price, x='year', y='close', hue='symbol', marker="o")
plt.title("Yearly Average Closing Price of Selected Stocks")
plt.ylabel("Average Closing Price")
plt.xlabel("Year")
plt.grid(True)
plt.tight_layout()
plt.show()

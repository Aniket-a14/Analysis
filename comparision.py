import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

# Here we check correlation between trading volume and closing price
correlation = df[['volume', 'close']].corr().iloc[0, 1]
print(f"Correlation between volume and closing price: {correlation:.2f}")

# Scatter plot for random 1000 rows
plt.figure(figsize=(10,6))
sns.scatterplot(data=df.sample(1000), x='volume', y='close', alpha=0.6)
plt.title("Volume vs Closing Price")
plt.xlabel("Volume")
plt.ylabel("Closing Price")
plt.tight_layout()
plt.show()

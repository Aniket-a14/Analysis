import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("S&P 500 Stock Prices 2014-2017.csv")
df['date'] = pd.to_datetime(df['date'])

aapl = df[df['symbol'] == 'AAPL']
aapl_2014 = aapl[aapl['date'].dt.year == 2014]['close']
aapl_2017 = aapl[aapl['date'].dt.year == 2017]['close']


t_stat, p_value = ttest_ind(aapl_2014, aapl_2017, equal_var=False)

print("Hypothesis Test: AAPL 2014 vs 2017 Closing Prices")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < 0.05:
    print("Conclusion: Closing price changed significantly between 2014 and 2017.")
else:
    print("Conclusion: No significant difference in closing price between 2014 and 2017.")

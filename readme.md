
# Stock Market Analysis on S&P 500 (2014–2017)

This project aims to perform data analysis on the stock prices of S&P 500 companies from 2014 to 2017. The dataset used for this analysis was sourced from Maven Analytics' Data Playground.

## 📁 Dataset Information

- **Source:** [Maven Analytics Data Playground](https://mavenanalytics.io/data-playground?order=date_added%2Cdesc&page=6&pageSize=5)
- **Columns:** `symbol`, `date`, `open`, `high`, `low`, `close`, `volume`
- **Rows:** 497,472
- **Period Covered:** 2014 to 2017

## 📊 Objectives

1. Test if average stock prices significantly increased from 2014 to 2017 using hypothesis testing.
2. Analyze sector-wise or company-wise stock price volatility using standard deviation of daily returns.
3. Visualize year-wise price trends of top-performing companies using line plots.
4. Compute correlation between stock prices of different companies to find similar movement patterns.
5. Compare stock price distributions across years using boxplots or KDE plots.

## 🔍 Folder Structure

```
📁 project_root/
├── analysis.py                 # EDA and basic stats
├── hypothesis_testing.py       # Hypothesis testing on stock prices
├── volatility_analysis.py      # Volatility analysis across companies
├── trend_visualization.py      # Line plots for year-wise trends
├── correlation_analysis.py     # Correlation analysis among companies
├── distribution_analysis.py    # Distribution comparison using boxplots
├── Stock_Market_Analysis_Report_Cover_Sections.docx  # DOCX Report Cover
├── README.md                   # This README file
```

## 🧰 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

## 📌 How to Run

Make sure you have Python installed along with the required libraries. Then run each Python file in the order of analysis or as required using:

```bash
python filename.py
```

## ✅ Author

- Name: Aniket Saha
- Reg No: 12314934
- Department of Computer Science & Engineering, Lovely Professional University

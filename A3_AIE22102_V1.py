import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

# Load the data from Excel file
file_path = "Lab Session1 Data.xlsx"
df_irctc = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")

# Task 1: Calculate the mean and variance of the Price data
price_data = df_irctc['Price']
mean_price = statistics.mean(price_data)
variance_price = statistics.variance(price_data)

print(f"Mean of Price data: {mean_price}")
print(f"Variance of Price data: {variance_price}")

# Task 2: Select the price data for all Wednesdays and calculate the sample mean
wednesday_data = df_irctc[df_irctc['Day'] == 'Wednesday']['Price']

if not wednesday_data.empty:
    sample_mean_wednesday = statistics.mean(wednesday_data)
    print(f"Sample mean of Wednesday price data: {sample_mean_wednesday}")
else:
    print("No data available for Wednesdays.")

# Task 3: Select the price data for the month of Apr and calculate the sample mean
april_data = df_irctc[df_irctc['Month'] == 'Apr']['Price']
sample_mean_april = statistics.mean(april_data)

print(f"Sample mean of April price data: {sample_mean_april}")

# Task 4: Find the probability of making a loss over the stock
loss_probability = np.mean(df_irctc['Chg%'].apply(lambda x: x < 0))
print(f"Probability of making a loss: {loss_probability}")

# Task 5: Calculate the probability of making a profit on Wednesday
wednesday_profit_probability = np.mean((df_irctc['Day'] == 'Wednesday') & (df_irctc['Chg%'] > 0))
print(f"Probability of making a profit on Wednesday: {wednesday_profit_probability}")

# Task 6: Calculate the conditional probability of making a profit, given that today is Wednesday
if not wednesday_data.empty:
    conditional_profit_probability = wednesday_data[wednesday_data > 0].count() / wednesday_data.count()
    print(f"Conditional probability of making profit on Wednesday: {conditional_profit_probability}")
else:
    print("No profit data available for Wednesdays.")


# Task 7: Scatter plot of Chg% data against the day of the week
plt.scatter(df_irctc['Day'], df_irctc['Chg%'])
plt.xlabel('Day of the Week')
plt.ylabel('Chg%')
plt.title('Scatter Plot of Chg% Data Against Day of the Week')
plt.show()

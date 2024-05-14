import pandas as pd
import matplotlib.pyplot as plt

sales_df = pd.read_excel('read_data.xlsx')

plt.figure(figsize=(8, 5))

plt.plot(sales_df['Month'], sales_df['Sale'], marker='.', linestyle='-', color='b', label='iPhone 16')

plt.xlabel('Month')
plt.ylabel('Sale in $')

plt.title('Sales by Month')

plt.grid(True)
plt.legend()

plt.show()

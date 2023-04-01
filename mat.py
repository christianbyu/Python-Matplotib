import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# fungsi coloumns
columns = ["month_number", "facecream", "facewash", "total_units", "total_profit"]
df = pd.read_csv("I:/My Drive/Tugas/Sem_4/03_Pengolahan_Data_Besar/Python-Matplotib/data/company_sales_data.csv", usecols=columns)

# Mencetak semua data yang ada pada fungsi coloumns
print(df)

# Mencetak Grafik untuk kolom facecream, facewash
plt.plot(df.month_number, df.facecream, df.facewash)
plt.show()

# Mencetak Grafik untuk kolom total_units, total_profit
plt.plot(df.month_number, df.total_units, df.total_profit)
plt.show()
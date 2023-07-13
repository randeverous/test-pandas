import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.ticker import NullFormatter

df = pd.read_excel(r'C:\Users\Lenovo\Documents\testSQL\Motocycles_sales\Penjualan_Honda.xlsx')
print(df)

df_Matic2019 = df[df['Tipe Motor'] == 'Matic']['2019'].sum()
print(df_Matic2019)
df_Matic2020 = df[df['Tipe Motor'] == 'Matic']['2020'].sum()
print(df_Matic2020)
df_Matic2021 = df[df['Tipe Motor'] == 'Matic']['2021'].sum()
print(df_Matic2021)
df_Matic2022 = df[df['Tipe Motor'] == 'Matic']['2022'].sum()
print(df_Matic2022)

def formatter(x, pos):
    return str(round(x / 1e6, 1))

x = ['2019', '2020', '2021', '2022']
y = [df_Matic2019, df_Matic2020, df_Matic2021, df_Matic2022]
penjualan_series=pd.Series(y)

plt.figure(figsize=(10, 7))
ax = penjualan_series.plot(kind="bar")
ax.set_title("Penjualan Motor Matic", y=1.05)
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Penjualan / unit")
ax.set_xticklabels(x, rotation=360)

ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_minor_formatter(NullFormatter())
ax.plot([1e6])
ax.text(0, 1.05, "dalam juta", transform = ax.transAxes, ha = "left", va = "top")

plt.show()


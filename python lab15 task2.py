import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)

df.fillna(0, inplace=True)

df['Month'] = df['Date'].dt.month

df['Total'] = df[['Rachel / Papineau', 'Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 'Brébeuf', 'Parc', 'CSC (Côte Sainte-Catherine)', 'PierDup']].sum(axis=1)

monthly_totals = df.groupby('Month')['Total'].sum()

popular_month = monthly_totals.idxmax()
print(f"Найпопулярніший місяць: {popular_month}")

monthly_totals.plot(kind='bar', color='orange', edgecolor='black')
plt.title('Кількість велосипедистів по місяцях')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=0)
plt.show()

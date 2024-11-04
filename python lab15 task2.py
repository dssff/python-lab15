import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)

df.fillna(0, inplace=True)

df['Month'] = df['Date'].dt.month

monthly_data = df.groupby('Month')[['Rachel / Papineau', 'Berri1', 'Maisonneuve_1', 
                                      'Maisonneuve_2', 'Brébeuf', 'Parc', 
                                      'CSC (Côte Sainte-Catherine)', 'PierDup']].sum()

monthly_data['Total'] = monthly_data.sum(axis=1)

popular_month = monthly_data['Total'].idxmax()
print(f"Найпопулярніший місяць: {popular_month}")

plt.figure(figsize=(15, 10))  
monthly_data.plot(kind='line', marker='o', ax=plt.gca())  
plt.title('Кількість велосипедистів по місяцях')
plt.xlabel('Місяць')
plt.xticks(range(1, 13))
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=1)  
plt.grid(axis='y')  
plt.legend(title='Велодоріжки')  
plt.show()
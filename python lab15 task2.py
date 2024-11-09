import pandas as pd
import matplotlib.pyplot as plt
import calendar

df = pd.read_csv('data.csv', parse_dates=['Date'], dayfirst=True)

df.fillna(0, inplace=True)

df['Month'] = df['Date'].dt.month

bike_paths = ['Rachel / Papineau', 'Berri1', 'Maisonneuve_1', 'Maisonneuve_2', 
              'Brébeuf', 'Parc', 'CSC (Côte Sainte-Catherine)', 'PierDup']

print("Доступні велосипедні доріжки:")
for idx, path in enumerate(bike_paths, 1):
    print(f"{idx}. {path}")

user_choice = int(input("виберіть велосипедну доріжку, ввівши відповідний номер "))
chosen_path = bike_paths[user_choice - 1]

monthly_data = df.groupby('Month')[chosen_path].sum()

popular_month = monthly_data.idxmax()
popular_month_value = monthly_data.max()

popular_month_name = calendar.month_name[popular_month]

print(f"Найпопулярніший місяць для велодоріжки {chosen_path}: {popular_month_name}")

plt.figure(figsize=(15, 10))
monthly_data.plot(kind='line', marker='o', ax=plt.gca())
plt.title(f'Кількість велосипедистів по місяцях для {chosen_path}')
plt.xlabel('Місяць')
plt.xticks(range(1, 13))
plt.ylabel('Кількість велосипедистів')
plt.xticks(rotation=1)
plt.grid(axis='y')
plt.legend(title='Велодоріжка')

plt.text(12.5, monthly_data.max() * 1.1,  
         f'Найпопулярніший місяць: {popular_month_name}', 
         fontsize=12, color='red', ha='right', va='center')

plt.show()
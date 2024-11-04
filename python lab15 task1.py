import pandas as pd

students = {
    "Чекмарьов Андрій Михайлович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 5.0,
            "Чисельні методи": 4.0,
            "ММДО": 4.5,
            "АТСД": 5.0,
            "Організація IT-бізнесу": 4.4
        }
    },
    "Ліцман Данііл Володимирович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 4.0,
            "Чисельні методи": 4.7,
            "ММДО": 4.8,
            "АТСД": 5.0,
            "Організація IT-бізнесу": 4.5
        }
    },
    "Майборода Єгор Андрійович": {
        "група": "КН31",
        "курс": 2,
        "оцінки": {
            "Пайтон": 4.8,
            "Чисельні методи": 5.0,
            "ММДО": 4.2,
            "АТСД": 4.7,
            "Організація IT-бізнесу": 4.8
        }
    },
    "Шевченко Станіслав Володимирович": {
        "група": "КН33",
        "курс": 2,
        "оцінки": {
            "Пайтон": 4.8,
            "Чисельні методи": 5.0,
            "ММДО": 4.2,
            "АТСД": 4.7,
            "Організація IT-бізнесу": 4.8
        }
    }
}

data = []
for student, info in students.items():

    data.append({
        "Прізвище та ім'я": student,
        "Група": info["група"],
        "Курс": info["курс"],
        **info["оцінки"] 
    })

df = pd.DataFrame(data)

print("Датафрейм студентів:")
print(df)

for student in df["Прізвище та ім'я"]:
    student_grades = df.loc[df["Прізвище та ім'я"] == student].iloc[:, 3:] 
    mean_grade = student_grades.mean(axis=1).values[0]  
    sum_grade = student_grades.sum(axis=1).values[0]  
    min_grade = student_grades.min(axis=1).values[0]  
    max_grade = student_grades.max(axis=1).values[0]  

    print(f"\nСтудент: {student}")
    print(f"Середнє значення оцінок = {mean_grade}")
    print(f"Сума оцінок = {sum_grade:.2f}")
    print(f"Мінімальна оцінка = {min_grade:.2f}")
    print(f"Максимальна оцінка = {max_grade:.2f}")

grouped_means = df.groupby('Група').mean(numeric_only=True)

print("\nСередні оцінки по групах:")
print(grouped_means)
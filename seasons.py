month = int(input("Введите номер месяца (от 1 до 12): "))

if month in [12, 1, 2]:
    season = "зима"
elif month in [3, 4, 5]:
    season = "весна"
elif month in [6, 7, 8]:
    season = "лето"
elif month in [9, 10, 11]:
    season = "осень"
else:
    season = "Неверный номер месяца!"

print(f"Этот месяц относится к времени года: {season}")

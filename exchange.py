dollars = float(input("Введите количество долларов: "))
exchange_rate = float(input("Введите текущий курс доллара: "))

hryvna = dollars * exchange_rate

print(f"Сумма в гривнах: {hryvna:.2f}")

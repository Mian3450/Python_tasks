import random

options = ["камень", "ножницы", "бумага"]

user_choice = input("Выберите: камень, ножницы или бумага: ").lower()

computer_choice = random.choice(options)

print(f"Компьютер выбрал: {computer_choice}")

if user_choice == computer_choice:
    print("Ничья!")
elif (user_choice == "камень" and computer_choice == "ножницы") or \
     (user_choice == "ножницы" and computer_choice == "бумага") or \
     (user_choice == "бумага" and computer_choice == "камень"):
    print("Вы победили!")
else:
    print("Вы проиграли!")

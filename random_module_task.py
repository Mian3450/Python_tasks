import random
random_number = random.randint(1, 10)
guess_number = int(input("Угадайте число от 1 до 10:  "))

if guess_number < random_number:
    print("Ваше число меньше загаданного.")
    print(f"Загаданное число было: {random_number}")
elif guess_number > random_number:
    print("Ваше число больше загаданного.")
    print(f"Загаданное число было: {random_number}")
else:
    print("Вы угадали!!!")
    print(f"Загаданное число было: {random_number}")
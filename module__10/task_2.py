print("Задача 2. Лестница")

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

stop = int(input("Введите число: "))
number = 0

for row in range(1, stop + 1):
    number += 1
    for col in range(number):
        print(row, end="\t")
    print()

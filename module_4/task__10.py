print("Задача 10. Максимальное число (по желанию)")

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно


n = "=" * 45
print(n)

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

if number_1 > number_2 and number_1 > number_3:
    print("Максимальное число ", number_2)
elif number_2 > number_1 and number_2 > number_3:
    print("Максимальное число ", number_2)
elif number_3 > number_1 and number_3 > number_2:
    print("Максимальное число ", number_3)
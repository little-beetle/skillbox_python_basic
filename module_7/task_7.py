print("Задача 7. Отрезок")

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

num_min = int(input("Введите первое число: "))
num_max = int(input("Введите второе число: "))
summ = 0
average = 0
for number in range(num_min, num_max + 1):
    if number % 3 == 0:
        summ += number
        average += 1
print("Среднее арифметическое", summ / average)


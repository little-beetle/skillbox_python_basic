print("Задача 6. Сумма факториалов")

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

import math

count = 0
number = int(input("Введите число: "))
for num in range(1, number + 1):
    count += math.factorial(num)
print(count)

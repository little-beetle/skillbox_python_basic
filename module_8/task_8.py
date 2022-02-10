print("Задача 8. Сумма ряда")

# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N

amount_series = 0
num_user = int(input("Введите число: "))

for degree in range(0, num_user + 1):
  amount_series += ((-1)**(degree)) * 1/(2**degree)

print("Ответ: ", amount_series)

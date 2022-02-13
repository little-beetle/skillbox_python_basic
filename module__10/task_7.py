print("Задача 7. Наибольшая сумма цифр")

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

seq_num = int(input('Введите количество чисел: '))
suma = 0
max_sum = 0
max_num = 0

for i in range(seq_num):
  number = int(input("Введите число: "))
  this_num = number
  while number > 0:
    suma += number % 10
    number //= 10
  if suma > max_sum:
    max_sum = suma
    max_num = this_num
  suma = 0
  this_num = 0

print(f"Число {max_num} имеет максимальную сумму цифр: {max_sum}")


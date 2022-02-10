print("Задача 9. Выражение")

#Дано число x.
#Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))

num_x = int(input("Введите число"))
numerator = 1
denominator = 1
res = True

for i in range(1, 7):
  numerator *= num_x - 2 ** i + 1
  denominator *= num_x - 2 ** i
  print("i", i)
  print("^",numerator)
  print("~",denominator)
  if denominator == 0:
    print("Ошибка (деление на 0 невозможно)")
    res = False
    break
if res:
  print(numerator / denominator)


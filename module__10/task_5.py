print("Задача 5. Простые числа")


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.

seq_num = int(input("Сколько будет чисел: "))
num_count = seq_num

for num in range(1, seq_num + 1):
  print(f"Введите {num}-e число:", end = " ")
  number = int(input())
  if number == 0 or number == 1:
    num_count -= 1
  for divider in range(2, number):
    if number % divider == 0:
      num_count -= 1
      break

print("Простых чисел в последовательности:", num_count)
print("Задача 6. Успеваемость в классе")

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

student = int(input("Введите количество количество учеников: "))
sum_excellent = 0
sum_good = 0
sum_bad = 0
for i in range(1, student + 1):
  grade = int(input("Введите оценку: "))
  if grade == 3:
    sum_bad += 1
  elif grade == 4:
    sum_good += 1
  else:
    sum_excellent += 1

if sum_excellent< sum_good > sum_bad:
  print("Хорошистов больше")
elif sum_good < sum_excellent > sum_bad:
  print("Отличников больше")
elif sum_good < sum_bad > sum_excellent:
  print("Троечников больше")

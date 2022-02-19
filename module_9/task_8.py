print("Задача 8. Колонтитул")

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку.

text = int(input("Какая длинна колонки? "))
importantly = int(input("На сколько важна? "))

left = round((text - importantly) / 2)
right = (text - importantly - left)

print("~" * left, end = "")
print("!" * importantly, end = "")
print("~" * right)

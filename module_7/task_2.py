print("Задача 2. Должники")

# Должники и законопослушные граждане хранятся в одной базе банка.
# Из этой базы нам выделяются по 10 человек, у каждого из которых есть свой номер.
# Правда, иногда база глючит и выдаёт нам отрицательный номер.
# А ещё по статистике, которую собрал наш МирПрогБанк,
# каждый второй, кто в этом году брал кредит, не выплатил его вовремя.
#
# Пользователь вводит 10 чисел.
# Напишите программу,
# которая определяет, сколько из них являются одновременно четными и положительными.
summ = 0
for i in range(10):
  num_user = int(input("Введите число "))
  if num_user % 2 == 0 and num_user > 0:
    summ += 1
print("Кол-во однодновеменно чётных и положительных чисел равна", summ)
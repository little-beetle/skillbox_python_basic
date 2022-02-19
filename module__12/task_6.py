print("Задача 6. Монетка")

# Практиканту дали задание
# найти старую металлическую монетку по заданным координатам.
#
# Металлоискатель сканирует местность вокруг пользователя
# и при обнаружении/отсутствии металла прибор отображает на экране соответствующее сообщение.
#
#
# Даны два действительных числа x и y.
# Напишите функцию, которая проверяет,
# принадлежит ли точка с координатами (x,y) заштрихованному квадрату (включая его границу).
# Если точка принадлежит квадрату,
# выведите сообщение “Монетка где-то рядом”,
# иначе выведите сообщение “Монетки в области нет”.
#
# На рисунке сетка проведена с шагом 1.
#
# P.S - Смотри рисунок на сайте :)
#         ^
#         |
#        *|*
# ========+=======>
#        *|*
#         |

def location(coordinate_x, coordinate_y):
  if -1 <= coordinate_x <= 1 and -1 <= coordinate_y <= 1:
    print("Монетка где-то рядом")
  else:
    print("Монетки в области нет")


coordinate_x = float(input("Введите координату х: "))
coordinate_y = float(input("Введите координату у: "))

location(coordinate_x, coordinate_y)
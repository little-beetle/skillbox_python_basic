print("Задача 9. Уравнение")

# Даны действительные коэффициенты a, b, c,
# при этом a≠0.
# Решите квадратное уравнение ax^2+bx+c=0 и выведите все его корни.
#
# Если уравнение имеет два корня,
# выведите два корня в порядке возрастания,
# если один корень — выведите одно число,
# если нет корней — не выводите ничего

import math

const_a = int(input("a: "))
const_b = int(input("b: "))
const_c = int(input("c: "))

discriminant = const_b ** 2 - 4 * const_a * const_c
if discriminant > 0:
  print(f"х_1 = {(-const_b + math.sqrt(discriminant)) / (2 * const_a)}\t х_2 = {(-const_b - math.sqrt(discriminant)) / (2 * const_a)}")
elif discriminant == 0:
  print("х =", -const_b / (2 * const_a))
else:
  print("Корней нет")
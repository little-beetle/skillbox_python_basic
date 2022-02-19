print("Задача 8. Сумма ряда")


# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def factorial_num(n):
    factorial = 1
    for num in range(1, n + 1):
        factorial *= num
    return factorial


def degree_num(x, n):
    count = 1
    for num in range(1, n + 1):
        count = count * x
    return count


def tast(x, precision):
    degree = 0
    add_num = 1
    result = 0
    while abs(add_num) > precision:
        add_num = degree_num(-1, degree) * (degree_num(x, (2 * degree)) / factorial_num(2 * degree))
        result += add_num
        degree += 1
    return result


x = int(input("Введите x: "))
precision = float(input("Введите точность: "))

print(tast(x, precision))

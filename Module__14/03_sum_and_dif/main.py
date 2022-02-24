def sum_num(number):
    summa = 0
    while number > 0:
        digit = number % 10
        summa += digit
        number = number // 10
    return summa


def num_digits(number):
    digits = 0
    while number > 0:
        number //= 10
        digits += 1
    return digits


number = int(input("Введите число: "))

print("Сумма цифр:", sum_num(number))
print("Кол-во цифр в числе:", num_digits(number))
print("Разность суммы и кол-ва цифр", sum_num(number) - num_digits(number))

# зачет!

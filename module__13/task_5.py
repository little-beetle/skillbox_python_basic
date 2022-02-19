print("Задача 5. Недоделка 2")

# Вы всё так же работаете в конторе по разработке игр
# и смотрите различные программы прошлого горе-программиста.
# В одной из игр для детей, связанной с мультяшной работой с числами,
# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и вам самим становится, мягко говоря, не по себе от него.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.


def check_1(num):
    num_count = 0
    while num > 0:
        num_count += 1
        num //= 10
    if num_count < 3:
        print("В первом числе меньше трёх цифр.")
        return False
    return num_count


def check_2(num):
    num_count = 0
    while num > 0:
        num_count += 1
        num //= 10
    if num_count < 4:
        print("Во втором числе меньше четырех цифр.")
        return False
    return num_count


def first_last_number(num, length):
    last_digit = num % 10
    first_digit = num // 10**(length - 1)
    between_digits = num % 10**(length - 1) // 10
    num = last_digit * 10**(length - 1) + between_digits * 10 + first_digit
    return num


number_1 = int(input("Введите первое число: "))
length_1 = check_1(number_1)

number_2 = int(input("\nВведите второе число: "))
length_2 = check_2(number_2)

while check_1(number_1) == False and check_2(number_2) == False:

    print("\nНеверные данные, побробуйте еще раз)")

    number_1 = int(input("Введите первое число: "))
    length_1 = check_1(number_1)

    number_2 = int(input("\nВведите второе число: "))
    length_2 = check_2(number_2)

else:
    print("Изменённое первое число:", first_last_number(number_1, length_1))

    print("Изменённое второе число:", first_last_number(number_2, length_2))

    print(
        "\nСумма чисел:",
        first_last_number(number_1, length_1) +
        first_last_number(number_2, length_2))

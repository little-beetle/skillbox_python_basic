print("Задача 4. Число наоборот")

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
#
# Введите число: 1000
# Число наоборот: 0001
#
# Введите число: 0
# Программа завершена!
#
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
#
# Введите число: 1230
# Число наоборот: 321
#
# Кстати, нули, которые мы убрали, называются ведущими.


def reversed_string(a_string):
    return a_string[::-1]


def main():
    number = input("Введите число: ")
    while number != "0":
        print(reversed_string(number.rstrip("0")))
        number = input("Введите число: ")
    print("Программа завершена!")


main()

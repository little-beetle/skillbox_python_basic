def separation_whole(number):
    flag = True
    whole = ""  # целое
    fraction = ""  # дробь
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    return int(whole)


def separation_fraction(number):
    flag = True
    whole = ""  # целое
    fraction = ""  # дробь
    for symbol in number:
        if symbol == '.':
            flag = False
        elif flag:
            whole += symbol
        else:
            fraction += symbol
    return int(fraction)


def revers(n):
    count = 0
    while n > 0:
        count = count * 10 + n % 10
        n //= 10
    return str(count)


def bonding(revers_whole, revers_fraction):
    revers_num = revers_whole + "." + revers_fraction
    return str(revers_num)


def sum_num(first_num, second_num):
    summa = float(first_num) + float(second_num)
    return summa


first_number = (input("Введите первое число: "))
second_number = (input("Введите второе число: "))

num_1_rev = bonding(revers(separation_whole(first_number)),
                    revers(separation_fraction(first_number)))
num_2_rev = bonding(revers(separation_whole(second_number)),
                    revers(separation_fraction(second_number)))

print(
    f"\nПервое число наоборот: {num_1_rev} "
    f"\nВторое число наоборот: {num_2_rev} ")

print(
    f"\nСумма: {sum_num(num_1_rev, num_2_rev)} ")

# зачет!

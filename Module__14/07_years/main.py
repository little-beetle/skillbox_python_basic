def four_num():
    num = int(input())
    if 999 > num < 10000:
        print("Вы ввели неподходящий год")
        return four_num()
    return num


def strange_year(num_1, num_2):
    for i in range(num_1, num_2 + 1):
        thousands = i // 1000
        hundreds = i // 100 % 10
        tens = i // 10 % 10
        unit = i % 10
        if (thousands == hundreds == tens) or (hundreds == tens == unit) or \
                (tens == unit == thousands) or (thousands == hundreds == unit):
            print(thousands * 1000 + hundreds * 100 + tens * 10 + unit)


print("Введите первый год: ")
num_1 = four_num()

print("Введите второй год: ")
num_2 = four_num()

strange_year(num_1, num_2)

# зачет!

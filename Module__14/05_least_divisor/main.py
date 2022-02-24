def small_divisor(num):
    i = 1
    while i <= num:
        i += 1
        if num % i == 0:
            break
    return i

number = int(input("Введите число: "))

print(f"Наименьший делитель, отличный от единицы: {small_divisor(number)}")

# зачет!

print("Задача 7. Банкомат")

# Пользователи банкомата хотят снимать деньги.
# Но банкомат умеет выдавать только купюры по 100 рублей.
# Напишите программу,
# которая проверяет допустимость суммы средств, которую ввёл пользователь.

# Пример:
# Введите сумму, которую хотите снять: 250
# Такую сумму снять невозможно. Обратитесь в другой банкомат.
n = "=" * 45
print(n)
x = int(input("Введите сумму, которую хотите снять: "))
if x % 100 == 0:
    print("Сейчас Вы получите деньги!")
else:
    print("Такую сумму снять невозможно. Обратитесь в другой банкомат.")

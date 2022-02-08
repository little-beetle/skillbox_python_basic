print("Задача 10. Игра «Компьютер угадывает число»")

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

print("Задача 10. Игра «Компьютер угадывает число»")

mystery = int(input("Загадайте число - "))
print("Поехали")
n_left = 0
n_right = 100
answer = 0
while answer != 1:
    answer = int(
        input(
            f"Ваше число равно(1), больше(2) или меньше(3): {(n_right + n_left) // 2}: "
        ))
    if answer == 2:
        n_left = (n_right + n_left) // 2
    elif answer == 3:
        n_right = (n_right + n_left) // 2
print("Угадали!")
print("Задача 3. Следим за зубами")

# Стоматолог посоветовал Маше использовать зубную нить каждый чётный день.
# Чтобы не забывать, Маша написала скрипт на Python,
# который в случае чего напоминает ей про совет стоматолога.
# Напишите программу, которая проверяет, чётное ли число ввёл пользователь,
# и выводит соответствующее сообщение.
# Подсказка: для проверки чётности используйте оператор %.
n = "=" * 45
print(n)
number = int(input("Введите сегоднешнюю дату, \nдля проверки четности/нечетности числа: "))
if number % 2 == 0:
    print("Четное число")
else:
    print("Нечентное число")
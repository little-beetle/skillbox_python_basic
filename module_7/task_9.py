print("Задача 9. ...Теперь можно посчитать и свою")

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
#
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
money = 0
score = 0
for number in range(1, 11):
    print('Месяц', number)
    money1 = int(input('Введите сумму вашей зарплаты:'))
    if money > money1:
        score += 1
    money = money1
if score > 0:
    print('Зарплата возрастает не упорядоченно...')



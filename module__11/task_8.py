print("Задача 8. Часы")

# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа.
# Входные и выходные данные — действительные числа.
#
# При решении этой задачи нельзя пользоваться условными операторами и циклами.

degree = float(input("Введите угол: "))
print("Ответ: ", degree % 30 * 12)
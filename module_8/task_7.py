print("Задача 7. Стипендия")

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant = int(input("Введите стипендию: "))
expenses = int(input("Введите расходы на проживание: "))
parents_money = 0

for i in range(10):
    parents_money += expenses - educational_grant
    expenses += expenses / 100 * 3

print("Просить надо ", round(parents_money, 2), "денге")
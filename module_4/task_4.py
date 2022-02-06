print("Задача 4. Калькулятор скидки")

# Андрей переехал на новую квартиру, и ему нужно купить три стула в разные комнаты.
# Естественно, цена на стулья в разных магазинах различается,
# а где-то ещё и скидка есть.
# Вот для одного из таких магазинов он и написал калькулятор скидки,
# чтобы проще ориентироваться в ценах.

# Напишите программу,
# которая запрашивает три стоимости товара и вычисляет сумму чека.
# Если сумма чека превышает 10 000 рублей,
# то нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100).
# В конце вывести итоговую сумму на экран.


n = "=" * 45
print(n)

product_1 = int(input("Введите стоимость первого товара: "))
product_2 = int(input("Введите стоимость второго товара: "))
product_3 = int(input("Введите стоимость третьего товара: "))

price = product_1 + product_2 + product_3

if price <= 10000:
    print("\nИтоговая сума:", price)
else:
    print("\nИтоговая сума со скидкой % 10:", price - (price * 10) / 100)

shop = [["каретка", 1200], ["шатун", 1000], ["седло", 300], ["педаль", 100], ["седло", 1500],
        ["рама", 12000], ["обод", 2000], ["шатун", 200], ["седло", 2700]]

details = 0
price_sum = 0
name_detail = input("Название детали: ")
for product, price in shop:
    if product == name_detail:
        details += product.count(name_detail)
        price_sum += price

print(f"\nКол-во деталей - {details} \nОбщая стоимость - {price_sum}")

# зачет!

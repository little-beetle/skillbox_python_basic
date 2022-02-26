main = [1, 5, 3]
first_lst = [1, 5, 1, 5]
second_lst = [1, 3, 1, 5, 3, 3]

main.extend(first_lst)

num_5 = main.count(5)

for i in main:
    if i == 5:
        main.remove(5)

main.extend(second_lst)

num_3 = main.count(3)

print("Кол-во цифр 5 при первом объьединени:", num_5)
print("Кол-во цифр 3 при втором объединении:", num_3)
print("Итоговый список:", main)

# зачет!

number = int(input("Кол-во коньков: "))
shoes_size = []
for i in range(1, number + 1):
    size = int(input(f"Размер {i} пары: "))
    shoes_size.append(size)

num_people = int(input("Кол-во людей: "))
feet_size = []
for i in range(1, num_people + 1):
    size_lag = int(input(f"Размер ноги {i} человека: "))
    feet_size.append(size_lag)

suitable_list = []
for index_shoes in range(number):
    for index_feet in range(num_people):
        if shoes_size[index_shoes] == feet_size[index_feet]:
            suitable_list.append(feet_size[index_feet])

unique_list = list(set(suitable_list))
print("\nНаибольшее кол-во людей, которые могут взять ролики:", len(unique_list))

# зачет!

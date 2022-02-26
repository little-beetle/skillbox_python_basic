first = []
second = []
for i in range(1, 4):
    number = int(input(f"Введите {i} число для первого списка: "))
    first.append(number)

for i in range(1, 8):
    number = int(input(f"Введите {i} число для второго списка: "))
    second.append(number)

first.extend(second)

print(list(set(first)))

# зачет!

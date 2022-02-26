num_friends = int(input("Кол-во друзей: "))
num_iou = int(input("Долговых расписок: "))
friends = []

for i in range(1, num_friends + 1):
    friends.append([i, 0])

for i in range(1, num_iou + 1):

    print(f"\n{i} расписка")

    people_1 = int(input("Кому: ")) - 1
    people_2 = int(input("От кого: ")) - 1
    money = int(input("Сколько: "))

    friends[people_2][1] += money
    friends[people_1][1] -= money

print("\nБаланс друзей:")

for i in range(num_friends):
    print(f"{i + 1} : {friends[i][1]}")

# зачет!

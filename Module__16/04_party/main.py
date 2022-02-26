friends = ["Петя", "Ваня", "Саша", "Лиза", "Катя"]
flag = True
while flag:
    print(f"Сейчас на вечеринке {len(friends)} человек: {friends}")
    action = input("Гость пришёл или ушёл? ")
    name = input("Имя гостя: ")
    if action == "пришёл":
        if len(friends) > 6:
            print(f"Прости, {name}, но мест нет.")
            friends.append(name)
        else:
            friends.append(name)
    elif action == "ушёл":
        friends.remove(name)
        print(f"\nПока, {name}!\n")
    elif action == "Пора спать":
        print("\nВечеринка закончилась, все легли спать.")

# зачет!

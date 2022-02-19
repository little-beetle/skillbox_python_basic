import random

print("Задача 9. Недоделка")


# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
#
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
#
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
#
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

def rock_paper_scissors():
    ver = 0
    while (ver == 0):
        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1
    if player == 1:
        print("Вы выбрали камень.")
    elif player == 2:
        print("Вы выбрали ножницы.")
    elif player == 3:
        print("Вы выбрали бумагу.")

    comp = random.randint(1, 3)
    if comp == 1:
        print("Компьютер выбрал камень.")
    elif comp == 2:
        print("Компьютер выбрал ножницы.")
    elif comp == 3:
        print("Компьютер выбрал бумагу.")
    # определяем победителя
    if player == comp:
        win = 0
    elif player == 1 and comp == 2:
        win = 1
    elif player == 1 and comp == 3:
        win = 2
    elif player == 2 and comp == 1:
        win = 2
    elif player == 2 and comp == 3:
        win = 1
    elif player == 3 and comp == 1:
        win = 1
    elif player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("Ничья!")
        rock_paper_scissors()
    elif win == 1:
        print("Победил игрок!")
    elif win == 2:
        print("Победил компьютер!")


def guess_the_number():
    num_computer = random.randint(1, 10)
    num_user = int(input("Введите число: "))
    attempts = 0
    while num_user != num_computer:
        if num_user > num_computer:
            print("Число меньше, чем нужно. Попробуйте еще раз!")
        else:
            print("Число больше, чем нужно. Попробуйте еще раз!")
        num_user = int(input("Введите число, которое загадал компьютер: "))
        attempts += 1

    print(f"Вы угадали! Это было число {num_computer}. Число попыток: {attempts}")


def mainMenu():
    # Здесь главное меню игры
    choice = int(input("Добро пожаловать!\n1 - 'Угадай число'\n2 - 'Камень, ножницы, бумага'\n"))
    if choice == 1:
        guess_the_number()
    elif choice == 2:
        rock_paper_scissors()
    else:
        print("Неверные данные, попробуйте еще раз!")
        mainMenu()


mainMenu()
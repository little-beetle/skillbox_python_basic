print("Задача 6. Поставьте оценку!")

# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению от −100 до 100.
# Ему захотелось сравнить количество положительных и отрицательных отзывов,
# для этого он заранее отфильтровал все отзывы так,
# чтобы в конце были те, которые равны нулю.

# Напишите программу,
# которая находит количество положительных
# и количество отрицательных чисел в последовательности.
# Последовательность заканчивается на числе 0.

# Пример:
# Введите число: −4
# Введите число: −90
# Введите число: 6
# Введите число: 0
# Кол-во положительных чисел: 1
# Кол-во отрицательных чисел: 2

num_user = int(input("Введите число: "))
positive_num = 0
negative_num = 0

while True:
    if num_user == 0:
      break
    elif num_user > 0:
        positive_num += 1
    else:
        negative_num += 1
    num_user = int(input("Введите число: "))

print(
    f"Кол-во положительных числе: {positive_num}\nКол-во отрицательных чисел: {negative_num}"
)

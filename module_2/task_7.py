print("Задача 7. Путь к файлу")

# Что нужно сделать
# К каждому файлу на компьютере можно узнать путь. Выглядит он примерно так:
# 'C:/user/docs/folder/file_name.txt'

# Напишите программу,
# которая запрашивает у пользователя его имя и имя файла (переменные user и file_name соответственно).
# Используя операцию конкатенации, выведете путь к файлу на экран.
# Пример результата:

# Введите ваше имя: Sasha
# Введите имя файла: text
# C:/Sasha/docs/folder/text.txt
x = "=" * 30
print(x)
name = input("Введите ваше имя: ")
name_file = input("Введите ваше имя: ")
print(x)
print("C:/" + name + "/docs/folder/" + name_file + ".txt")

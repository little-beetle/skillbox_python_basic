
print("Задача 6. Спецшифр")

# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”,
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
#
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
#
# Пример:
# Введите строку: ssbbssbsbc
# Самая длинная последовательность: 3

string = input("Вводите строку: ")
count = 0
num = 0

for i in string:
    if i == "s":
        count += 1
    else:
        if count > num:
            num = count
            count = 0

print("Самая длинная последовательность:", num)

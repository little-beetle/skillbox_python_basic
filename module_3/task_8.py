print("Задача 8. Режем число на части")

# Реализуйте программу,
# которая получает на вход четырёхзначное число
# и выводит на экран каждую его цифру отдельно
# (в одну строчку либо каждая цифра в новой строчке).
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных

n = ("=") * 30
print(n)
number = int(input("Введите четырёхзначное число: "))
index_1 = number // 1000
index_2 = number // 100 % 10
index_3 = number % 100 // 10
index_4 = number % 10

print(f"Ответ:\n{index_1} {index_2} {index_3} {index_4}")

print("Задача 4. Площадь треугольника")

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула:
# S = ab/2

n = "=" * 30

print(n)
print("Прямоугольный треугольник:")

for i in range(6):
    print('* ' * i)

print("\nФормула: ")
print("S = (a * b) / 2")
print(n)

a = int(input("Введите значение катета 'a': "))
b = int(input("Введите значение катета 'b': "))

square = (a * b) / 2

print(f"Площадь прямоугольного треугольника равна: \n{square}")

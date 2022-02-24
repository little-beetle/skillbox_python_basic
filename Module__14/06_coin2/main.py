def found(x, y, radius):
    if x ** 2 + y ** 2 <= radius ** 2:
        print("Монетка где-то рядом")
    else:
        print("Монетки в области нет")


print("Введите координаты монетки:")
x = float(input("X: "))
y = float(input("Y: "))
radius = float(input("Введите радиус: "))

found(x, y, radius)

# зачет!

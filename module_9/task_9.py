print("Задача 9. Коровы")

# Для коров есть 10 стойл.
# В каждом стойле разные условия для животных, поэтому и молока они дают по-разному.
# В первом стойле производят 2 литра в день,
# во втором 4,
# в третьем - 6, потом 8, 10, 12, 14, 16, 18, 20.
# Но коровы стоят не во всех стойлах.
# Свободные и занятые обозначаются строкой из букв a и b,
# где a - свободное стойло, b - занятое.
#
# Пользователь вводит строку из 10 символов a и b.
# Необходимо определить, сколько в итоге будет произведено молока за день.

milk = 0

for i in range(1, 11):
  stall = input(f"{i} стойло свободное?\na - да \tb - нет\n")
  if stall == "a":
    milk += i * 2

print(f"За день будет произведено {milk} литров молока")
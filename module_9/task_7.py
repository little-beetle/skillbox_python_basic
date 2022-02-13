print("Задача 7. Великий и могучий")

# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
#
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
#
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5
text = input("Введите текст: ").split()
max_len = 0

for word in text:
    word_len = 0
    for letter in word:
        word_len += 1
    if word_len > max_len:
        max_len = word_len

print(f"Длина самого длинного слова: {max_len}")
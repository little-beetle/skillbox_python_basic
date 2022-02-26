def s_sort(array_1, array_2):
	general_class = []

	for i in range(len(array_1 + array_2)):
		if len(array_1) == 0:
			general_class.append(min(array_2))
			array_2.remove(min(array_2))
		elif len(array_2) == 0:
			general_class.append(min(array_1))
			array_1.remove(min(array_1))
		elif min(array_1) <= min(array_2):
			general_class.append(min(array_1))
			array_1.remove(min(array_1))
		elif min(array_1) > min(array_2):
			general_class.append(min(array_2))
			array_2.remove(min(array_2))
	return general_class


first_class = list(range(162, 177, 2))
second_class = list(range(162, 181, 3))

print("Отсортированный список учеников:", *s_sort(first_class, second_class))

# зачет!

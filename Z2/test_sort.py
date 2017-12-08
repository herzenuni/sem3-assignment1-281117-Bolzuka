# Практичское задание Z2
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача 2
#
# ЧАСТЬ 1
#
# Найдите все двузначные и трехзначные числа, сумма квадратов цифр которых делится на 17.
# Для двузначных чисел ответом будет следующий список: 14, 28, 29, 35, 41, 53, 67, 76, 82, 92
# Протестируйте программу. Тесты оформить с помощью pytest или UnitTest.


from Z2 import sum_number_in_2

def test_1():
	lst = list()
	for i in range(10, 100):
		if sum_number_in_2(i) % 17 == 0:
			lst.append(i)
	assert(lst == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])

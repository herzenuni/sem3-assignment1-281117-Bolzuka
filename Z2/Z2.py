# Практичское задание Z2
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача 2
#
# ЧАСТЬ 1
#
# Найдите все двузначные и трехзначные числа, сумма квадратов цифр которых делится на 17.
# Для двузначных чисел ответом будет следующий список: 14, 28, 29, 35, 41, 53, 67, 76, 82, 92
# Протестируйте программу. Тесты оформить с помощью pytest или UnitTest.

def sum_number_in_2(number):
	number = str(number)
	sum = 0
	for ch in number:
		sum = sum + int(ch) ** 2
	return sum

def fun():
	n = int(input("n = "))
	print("{}значные числа, сумма квадратов цифр которых делится на 17:". format(n))
	for i in range(10 ** (n - 1), 10 ** n):
		if sum_number_in_2(i) % 17 == 0:
			print(i, end = ', ')
	print()

	fun()

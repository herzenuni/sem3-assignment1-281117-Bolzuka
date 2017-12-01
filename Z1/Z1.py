# Практичское задание Z1
# Шибаева Мария Дмитриевна|  ИВТ | 2 курс | 1 подгруппа
# Задача 1
#
# ЧАСТЬ 1
#
# Вычислите сумму цифр данного натурального числа. Требования к программе:
# число вводит пользователь;
# число может иметь различное число знаков;
# ввод с клавиатуры и вывод результата оформить в виде отдельной функции, вывод оформить с помощью метода format;
# вычисление суммы цифр оформить в виде отдельной функции;
# тесты оформить с помощью pytest, реализовав тесты параметризованными и в отдельном файле.



def v():
    number = int(input("Enter the number = "))
    return number

def sum_number(number):
	number = str(number)
	sum = 0
	for ch in number:
		sum = sum + int(ch)
	return sum

def vv(number):
	print("Sum of numbers {} = {}".format(number, sum_number(number)))


#number = v()
#vv(number)
vv(sum_number(v()))

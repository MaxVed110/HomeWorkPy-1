# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]


def Factorial(number):
    res = 1
    list = []
    if number == 0 or number == 1:
        print("Последовательности нет, факториал равен 1")
    else:
        for i in range(1, number+1):
            res *= i
            list.append(res)
        print(f"Факториал-последовательность заданного числа: {list}")


num = 7
Factorial(num)

# Подсчитать сумму цифр в вещественном числе.

def CounterSum(number):
    sum = 0
    if number % 1 != 0:
        while number % 1 != 0:
            number *= 10
    while number != 0:
        sum += int(number % 10)
        number = int(number/10)
    return sum


numberUser = 1234.91
sum = CounterSum(numberUser)
print(sum)

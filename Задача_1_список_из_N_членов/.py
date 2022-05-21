#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

def GeometricSequence(number):
    if number == 0:
        print("Последовательность не задана")
    else:
        count =1
        list =[count]
        for i in range(number-1):
            count*=(-3)
            list.append(count)
        print(f"Последовательность чисел: {list}")
    

print("Задайте число >0")
numberUser = int(input())
GeometricSequence(numberUser)

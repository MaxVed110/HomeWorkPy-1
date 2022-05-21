#Определить количество вхождений одной строки в другую

import string


print("Введите первую строку")
stringUser = input()
print("Введите вторую строку")
substring = input()

result = stringUser.count(substring)
print(f"Количество вхождений первой строки во вторую равно: {result}")

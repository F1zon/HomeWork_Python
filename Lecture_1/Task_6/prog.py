# Задача 6:
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета

# Примеры:
# 385916 -> yes
# 123456 -> no

num = int(input("Введите число: "))

x = num // (10 ** 5)
y = (num // (10 ** 4)) % 10
z = (num // (10 ** 3)) % 10
firstSum = x + y + z

g = (num // (10 ** 2)) % 10
h = (num // 10) % 10
j = num % 10
twoSum = g + h + j

if firstSum == twoSum:
    print("yes")
else:
    print("no")
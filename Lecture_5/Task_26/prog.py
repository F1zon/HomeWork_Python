# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def con(num, dis):
    if dis > 1:
        return con(num, dis - 1) * con(num, 1)
    return num

num = int(input("Введите число: "))
dis = int(input("Введите степень: "))

print("Ваше число: {}".format(con(num, dis)))

# # Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# # 2 2
# # 4

def sums(a, b):
    if b != 0:
        a += 1
        b -= 1
        return sums(a, b)
    else:
        return a

a = int(input("Введите число: "))
b = int(input("+ ==> "))

print("сумма чисел {} + {} = {}".format(a, b, sums(a, b)))
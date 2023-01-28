# Задача 2: Найдите сумму цифр трехзначного числа.
# Примеры:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Enter numbers: '))

one = num // 100
two = (num % 100) // 10
three = num % 10
sums = one + two + three

print("Сумма чисел ({} + {} + {}) в числе {} = {}".format(one, two, three, num, sums))
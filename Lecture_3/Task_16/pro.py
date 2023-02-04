# Найти кол-во определённого элемента в списке

n = int(input("Введите размер списка: "))
num = 0
numList = []

print("Введите {} чисел:".format(n))
for i in range(n):
    num = int(input(":>> "))
    numList.append(num)

search = int(input("Какое число нужно найти: "))
x = 0

for i in range(n):
    if numList[i] == search:
        x += 1

print("Число {} встречается в списке {} раза".format(search, x))
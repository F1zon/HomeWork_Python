# Найти ближайший к числу элемент

n = int(input("Введите размер списка: ")) + 1
if n < 1:
    print("Недопустимая величина ERROR!")
    exit(1)

numList = []
for i in range(n):
    numList.append(i)

print(numList)
search = int(input("По какому числу искать: "))
num = 0

if (search < n + 1) and (search > 0):
    for i in range(n):
        if (numList[i] == search - 1) or (numList == search + 1):
            num = numList[i]
    print("Ближайшее число", num)
else:
    print("Число {} не родходит для массива".format(search))

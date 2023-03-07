# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# Пример: print_operation_table(lambda x, y(row and colums): x * y(operation))


# def print_operation_table(operation, row = 6, colums = 6):
#     str = []
#     for i in range(1, colums + 1):
#         for j in range(1, row + 1):
#             str.append(operation(i, j))
#         print(str)
#         str = []

def print_operation_table(operation, row = 6, colums = 6):
    table = []
    for i in range(1, colums + 1):
        table = [operation(i, j) for j in range(1, colums + 1)]
        print(*table, sep='\t')


print_operation_table(lambda x, y: x * y)
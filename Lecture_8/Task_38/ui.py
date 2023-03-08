from logger import print_date, input_date, filter_data

def interface():
    print("""Выберете режим работы программы: 
            1 - Запись данных;
            2 - Просмотр данных;
            3 - Поиск данных;
            """)
    comand = int(input("Введите номер команды: "))

    while comand < 1 or comand > 3:
        print("Введите корректный номер команды: ")
        comand = int(input("Введите номер команды: "))

    if comand == 1:
        input_date()
    elif comand == 2:
        print_date()
    elif comand == 3:
        print("Введите строку поиска через ';' :")
        filter_string = input(":>> ")
        filter_data(filter_string)

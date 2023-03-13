from logger import print_date, input_date, filter_data, change_data, delete_data

def interface():
    print("""Выберете режим работы программы: 
            1 - Запись данных;
            2 - Просмотр данных;
            3 - Поиск данных;
            4 - Изменение данных;
            5 - Удаление данных
            """)
    comand = int(input("Введите номер команды: "))

    while comand < 1 or comand > 5:
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
    elif comand == 4:
        change_data()
    elif comand == 5:
        delete_data()

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных
import os
from data_create import name_data, surname_data, adress_data, phone_data

file_name = "data.txt"

def print_date():
    if os.path.exists(file_name):
        print("Вывод мега Данных из файла: ")

        with open(file_name, 'r', encoding="utf-8") as file:
            list_data = file.readlines()
            count = 1
            for i in list_data:
                print(f"[{count}]: {i}")
                count += 1
    else:
        print("Файл не существует!!")

def input_date():
    print("Введите данные: ")
    name = name_data()
    surname = surname_data()
    adress = adress_data()
    phone = phone_data()

    with open(file_name, 'a', encoding="utf-8") as file:
        file.write(f"{name}; {surname}; {phone}; {adress}\n")


def filter_data(filter_string):
        with open(file_name, 'r', encoding="utf-8") as file:
            list_date = file.readlines()
            if ";" in filter_string:
                list_filter = filter_string.split(";")
            else:
                list_filter = [filter_string]
            is_found = False

            for element in list_date:
                temp_record = element.split(";")
                count = 0
                for record in temp_record:
                    for element_filter in list_filter:
                        if element_filter.lower() in record.lower() and len(element_filter) == len(record):
                            count += 1
                if count == len(list_filter):
                    print(element)
                    is_found = True
            
            if not is_found:
                print("Записей не найденно!")


def change_data():
    print_date();
    with open(file_name, 'r', encoding="utf-8") as file:
        old_list_data = file.readlines()
    
    print("Введите номер изменяемой строки: ");
    num = int(input(":>> "))

    while num < 1 or num > len(old_list_data):
        print("Введите имеющийся номер строки!!")
        num = int(input(":>> "))
    
    print("Что хотите изменить?")
    print("""
        1 - имя
        2 - фамилию
        3 - номер
        4 - адресс
    """)
    num_redactData = int(input(":>> "))

    while num_redactData < 1 or num_redactData > 4:
        print("Введите корректный номер операции!!")
        num_redactData = int(input(":>> "))

    # Отправление №операции, old_data, new_data
    if num_redactData == 1:
        new_data = name_data()
        operation_redact(num_redactData, new_data, old_list_data, num)
    elif num_redactData == 2:
        new_data = surname_data()
        operation_redact(num_redactData, new_data, old_list_data, num)
    elif num_redactData == 3:
        new_data = phone_data()
        operation_redact(num_redactData, new_data, old_list_data, num)
    elif num_redactData == 4:
        new_data = adress_data()
        operation_redact(num_redactData, new_data, old_list_data, num)

# Дополнительная функция для редактирования строк
def operation_redact(operation, new_data, old_data, num):
    with open(file_name, 'w', encoding="utf-8") as file:
        count = 1
        for i in old_data:
            if num == count:
                if operation == 1:
                    new_list = i.split("; ")
                    file.write(f"{new_data}; {new_list[1]}; {new_list[2]}; {new_list[3]}")
                elif operation == 2:
                    new_list = i.split("; ")
                    file.write(f"{new_list[0]}; {new_data}; {new_list[2]}; {new_list[3]}")
                elif operation == 3:
                    new_list = i.split("; ")
                    file.write(f"{new_list[0]}; {new_list[1]}; {new_data}; {new_list[3]}")
                elif operation == 4:
                    new_list = i.split("; ")
                    file.write(f"{new_list[0]}; {new_list[1]}; {new_list[2]}; {new_data}")
            else:
                file.write(i)
            count += 1

def delete_data():
    print_date()
    with open(file_name, 'r', encoding="utf-8") as file:
        old_list_data = file.readlines()
        print("Введите номер удаляемой строки: ")
        num = int(input(":>> "))

        while num < 1 or num > len(old_list_data):
            print("Введите имеющийся номер строки!!")
            num = int(input(":>> "))

    with open(file_name, 'w', encoding="utf-8") as file:
        count = 1

        for i in old_list_data:
            if num != count:
                file.write(i)
            count += 1

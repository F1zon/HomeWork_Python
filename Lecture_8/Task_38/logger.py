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


def change_data(): # Дополнить конкретные изменения
    print_date();
    with open(file_name, 'r', encoding="utf-8") as file:
        print("Введите номер изменяемой строки: ");
        num = int(input(":>> "))
        old_list_data = file.readlines()
    
    with open(file_name, 'w', encoding="utf-8") as file:
        print("Введите новые данные: ")
        name = name_data()
        surname = surname_data()
        adress = adress_data()
        phone = phone_data()

        count = 1
        for i in old_list_data:
            if num == count:
                file.write(f"{name}; {surname}; {phone}; {adress}\n")
            else:
                file.write(i)
            count += 1

def delete_data(): # Нер работает
    print_date()
    with open(file_name, 'r', encoding="utf-8") as file:
        print("Введите номер удаляемой строки: ")
        num = int(input(":>> "))
        old_list_data = file.readlines()
    
    with open(file_name, 'w', encoding="utf-8") as file:
        count = 1

        for i in old_list_data:
            if num == count:
                file.write("")
            else:
                file.write(i)

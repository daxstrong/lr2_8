#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime


def exit_program():
    """
    Выход из программы.
    """
    sys.exit()


def add_person(people):
    """
    Добавление информации о человеке.
    """
    last_name = input("Фамилия: ")
    first_name = input("Имя: ")
    phone_number = input("Номер телефона: ")
    birthdate_str = input("Дата рождения (в формате ДД.ММ.ГГГГ): ")
    birthdate = datetime.strptime(birthdate_str, "%d.%m.%Y")

    person = {
        'фамилия': last_name,
        'имя': first_name,
        'номер телефона': phone_number,
        'дата рождения': birthdate,
    }

    people.append(person)
    people.sort(key=lambda x: x['фамилия'])


def list_people(people):
    """
    Вывод списка всех людей.
    """
    line = f'+-{"-" * 25}-+-{"-" * 15}-+-{"-" * 25}-+'
    print(line)
    print(f"| {'Фамилия':^25} | {'Имя':^15} | {'Дата рождения':^25} |")

    for person in people:
        print(line)
        print(f"| {person['фамилия']:^25} | {person['имя']:^15} | {person['дата рождения'].strftime('%d.%m.%Y'):^25} |")
    print(line)


def select_people_by_month(people, month_to_search):
    """
    Вывод людей с днем рождения в указанном месяце.
    """
    found = False

    print(f"Люди с днем рождения в месяце {month_to_search}:")
    for person in people:
        if person['дата рождения'].month == month_to_search:
            print(
                f"Фамилия: {person['фамилия']}, Имя: {person['имя']}, Дата рождения: {person['дата рождения'].strftime('%d.%m.%Y')}")
            found = True

    if not found:
        print("Нет людей с днем рождения в указанном месяце.")


def help_info():
    """
    Вывод справочной информации о командах.
    """
    print("Список команд:\n")
    print("add - добавить информацию о человеке;")
    print("list - вывести список всех людей;")
    print("select <месяц> - вывести людей с днем рождения в указанном месяце;")
    print("exit - завершить работу с программой.")


if __name__ == '__main__':
    people = []

    while True:
        command = input(">>> ").lower()

        match command:
            case 'exit':
                exit_program()
            case 'add':
                add_person(people)
            case 'list':
                list_people(people)
            case command if command.startswith('select '):
                month_to_search = int(command.split(' ')[1])
                select_people_by_month(people, month_to_search)
            case 'help':
                help_info()
            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)

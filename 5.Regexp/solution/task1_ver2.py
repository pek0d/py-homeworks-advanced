import csv
import re
from pprint import pprint


# читаем адресную книгу в формате CSV в список contacts_list
def read_csv():
    with open("../phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


# pprint(contacts_list)


def process_contacts(contact) -> None:
    """Функция для обработки контакта"""
    name = contact[0].split()
    if len(name) > 0:
        contact[0] = name[0]  # Фамилия
    if len(name) > 1:
        contact[1] = name[1]  # Имя
    if len(name) > 2:
        contact[2] = " ".join(name[2:])  # Отчество


def split_name(full_name) -> list:
    """Функция для разделения полного имени на отчество, имя и фамилию"""
    return full_name.split()


def extract_names(contacts_list) -> list:
    """Функция для извлечения имен из списка контактов"""
    for row in contacts_list:
        full_name = " ".join(
            row[:3]
        )  # Объединяем фамилию, имя и отчество в одну строку
        processed_name = split_name(
            full_name
        )  # Разделяем полное имя на отдельные части: фамилию, имя и отчество
        row[
            :3
        ] = processed_name  # Обновляем список контакта с разделенными частями имени
        process_contacts(
            row
        )  # Обрабатываем контакт, соответственно вызывая функцию process_contacts
    return contacts_list


def remove_duplicates(contacts_list) -> list:
    """Удаление дублирующихся контактов и форматирование телефонных номеров"""
    seen_names = set()
    cleaned_contacts = []

    for contact in contacts_list:
        name = (
            contact[0],
            contact[1],
        )  # Создаем кортеж (имя, фамилия) для использования в качестве ключа
        if name not in seen_names:
            seen_names.add(
                name
            )  # Добавляем комбинацию (имя, фамилия) в множество уже увиденных имен

            cleaned_contacts.append(
                contact
            )  # Добавляем контакт в список обновленных контактов

    return cleaned_contacts


def write_cleaned_contacts(cleaned_contacts) -> None:
    """Функция для записи обновленного списка контактов без дубликатов в файл"""
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(cleaned_contacts)


if __name__ == "__main__":
    contacts_list = read_csv()
    extract_names(contacts_list)
    cleaned_contacts = remove_duplicates(contacts_list)
    write_cleaned_contacts(cleaned_contacts)

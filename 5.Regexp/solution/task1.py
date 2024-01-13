import csv
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
with open("../phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(contacts_list)


def process_contacts(names_list) -> None:
    """Функция для обработки списка контактов"""

    for contact in names_list:
        name = contact.split()
        print(name)
        # name_parts = name.split(" ")
        if len(name) > 0:
            names_list[0] = name[0]  # Last name
        if len(name) > 1:
            names_list[1] = name[1]  # First name
        if len(name) > 2:
            names_list[2] = " ".join(name[2:])  # Surname
    return names_list


def split_name(names_list) -> list:
    """Функция для разделения полного имени на отчество, имя и фамилию"""

    full_name = ["", "", ""]
    start = 0
    for name in names_list:
        if name:
            name = name.split()
            stop = len(name)
            full_name[start : start + stop] = name
            start += stop
    return full_name


def remove_duplicates(contacts_list) -> list:
    """Удаление дублирующихся контактов"""

    cleaned_contacts = []
    seen_names = set()

    for contact in contacts_list:
        name = (contact[0], contact[1])
        if name not in seen_names:
            cleaned_contacts.append(contact)
            seen_names.add(name)

    return cleaned_contacts


# Обработка контактов
# process_contacts(contacts_list)
def extract_names(contacts_list) -> list:
    """Функция для извлечения имен из списка контактов"""
    for row in contacts_list:
        row[:3] = process_contacts(row[:3])
        row[3:] = split_name(row[3:])

    return contacts_list


# for row in contacts_list:
#     # print(process_contacts(row[:3]))
#     print(split_name(row[:3]))

cleaned_contacts = remove_duplicates(contacts_list)  # Удаление дублирующихся контактов


def write_cleaned_contacts(cleaned_contacts) -> None:
    """Функция для записи обновленного списка контактов без дубликатов в файл"""
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(cleaned_contacts)


if __name__ == "__main__":
    extract_names(contacts_list)
    write_cleaned_contacts(cleaned_contacts)

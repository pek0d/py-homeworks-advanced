import csv
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
with open("../phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pprint(contacts_list)


def process_contacts(contacts_list) -> None:
    """Функция для обработки списка контактов"""
    for contact in contacts_list:
        name = contact[0]
        name_parts = name.split(" ")
        if len(name_parts) > 0:
            contact[0] = name_parts[0]  # Last name
        if len(name_parts) > 1:
            contact[1] = name_parts[1]  # First name
        if len(name_parts) > 2:
            contact[2] = " ".join(name_parts[2:])  # Surname


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
process_contacts(contacts_list)
cleaned_contacts = remove_duplicates(contacts_list)  # Удаление дублирующихся контактов


def write_cleaned_contacts(cleaned_contacts) -> None:
    """Функция для записи обновленного списка контактов без дубликатов в файл"""
    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(cleaned_contacts)


if __name__ == "__main__":
    write_cleaned_contacts(cleaned_contacts)

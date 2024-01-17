import csv
import re

with open("../phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


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

    result_dict = {}
    for row in contacts_list:
        key = row[0], row[1]
        data_dict = {
            "surname": row[2],
            "organization": row[3],
            "position": row[4],
            "phone": row[5],
            "email": row[6],
        }
        if result_dict.get(key):
            for value in result_dict.get(key):
                if row[2] in value.get("surname"):
                    value.update(
                        {key: data_dict.get(key) for key in value if not value.get(key)}
                    )
                else:
                    result_dict.get(key).append(data_dict)
        else:
            result_dict[key] = [data_dict]
    return result_dict


def extract_names(contacts_list) -> list:
    """Функция для извлечения имен из списка контактов"""

    for row in contacts_list:
        row[:3] = split_name(row[:3])
        row[5] = format_phone_number(row[5])
    return contacts_list


def format_phone_number(phone):
    """Функция для форматирования телефонного номера"""

    pattern = r"\+?([7|8])\s?\(?(\d{3})\)?[\s-]?(\d{3,})\-?(\d{2,})\-?(\d{2,})\s?\(?(\w{3})?\.?\s?(\d{4})?\)?"
    formatted_number = re.sub(pattern, r"+7(\2) \3-\4-\5 \6 \7", phone)
    return formatted_number


def write_contacts(result_dict, header) -> None:
    """Функция для записи обновленного списка контактов без дубликатов в файл"""

    with open("phonebook.csv", "w", encoding="utf-8", newline="") as f:
        datawriter = csv.DictWriter(f, fieldnames=header, delimiter=",")
        datawriter.writeheader()
        for key, value_list in result_dict.items():
            for value in value_list:
                datawriter.writerow(
                    {
                        "lastname": key[0],
                        "firstname": key[1],
                        "surname": value.get("surname"),
                        "organization": value.get("organization"),
                        "position": value.get("position"),
                        "phone": value.get("phone"),
                        "email": value.get("email"),
                    }
                )


if __name__ == "__main__":
    extract_names(contacts_list[1:])
    remove_duplicates_dict = remove_duplicates(contacts_list[1:])
    header = contacts_list[0]
    write_contacts(remove_duplicates_dict, header)

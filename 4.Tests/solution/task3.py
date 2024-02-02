def get_all_list(mentors):
    mentors = [
        [
            "Евгений Шмаргунов",
            "Олег Булыгин",
            "Дмитрий Демидов",
        ],
        [
            "Филипп Воронов",
            "Анна Юшина",
            "Иван Бочаров",
        ],
        [
            "Евгений Шмаргунов",
            "Олег Булыгин",
            "Александр Бардин",
        ],
        [
            "Владимир Чебукин",
            "Эдгар Нуруллин",
            "Евгений Шек",
        ],
    ]
    all_list = []
    for m in mentors:
        all_list.extend(m)
    return all_list


def get_all_names(all_list):
    all_list = [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Дмитрий Демидов",
        "Филипп Воронов",
        "Анна Юшина",
        "Иван Бочаров",
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Александр Бардин",
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
    ]

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    return all_names_list


def get_unique_names(all_names_list):
    all_names_list = [
        "Евгений",
        "Олег",
        "Дмитрий",
        "Филипп",
        "Анна",
        "Иван",
        "Евгений",
        "Олег",
        "Александр",
        "Владимир",
        "Эдгар",
        "Евгений",
    ]
    unique_names = set(all_names_list)
    result_string = ", ".join(sorted(unique_names))
    return result_string


if __name__ == "__main__":
    get_all_list(mentors)

courses = [
    "Java-разработчик с нуля",
    "Fullstack-разработчик на Python",
    "Python-разработчик с нуля",
    "Frontend-разработчик с нуля",
]
mentors = [
    [
        "Филипп Воронов",
        "Анна Юшина",
        "Иван Бочаров",
        "Анатолий Корсаков",
        "Юрий Пеньков",
        "Илья Сухачев",
        "Иван Маркитан",
        "Ринат Бибиков",
        "Вадим Ерошевичев",
        "Тимур Сейсембаев",
        "Максим Батырев",
        "Никита Шумский",
        "Алексей Степанов",
        "Денис Коротков",
        "Антон Глушков",
        "Сергей Индюков",
        "Максим Воронцов",
        "Евгений Грязнов",
        "Константин Виролайнен",
        "Сергей Сердюк",
        "Павел Дерендяев",
    ],
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Александр Бардин",
        "Александр Иванов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Роман Гордиенко",
        "Адилет Асканжоев",
        "Александр Шлейко",
        "Алена Батицкая",
        "Денис Ежков",
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Максим Филипенко",
        "Елена Никитина",
    ],
    [
        "Евгений Шмаргунов",
        "Олег Булыгин",
        "Дмитрий Демидов",
        "Кирилл Табельский",
        "Александр Ульянцев",
        "Александр Бардин",
        "Александр Иванов",
        "Антон Солонилин",
        "Максим Филипенко",
        "Елена Никитина",
        "Азамат Искаков",
        "Роман Гордиенко",
    ],
    [
        "Владимир Чебукин",
        "Эдгар Нуруллин",
        "Евгений Шек",
        "Валерий Хаслер",
        "Татьяна Тен",
        "Александр Фитискин",
        "Александр Шлейко",
        "Алена Батицкая",
        "Александр Беспоясов",
        "Денис Ежков",
        "Николай Лопин",
        "Михаил Ларченко",
    ],
]
durations = [14, 20, 12, 20]


# В этот список будут добавляться словари-курсы
def create_course_list(courses, mentors, durations):
    courses_list = []
    # Допишите код, который генерирует словарь-курс с тремя ключами:
    # "title", "mentors", "duration"
    for course, teacher, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": teacher, "durations": duration}
        courses_list.append(course_dict)
    return courses_list


def get_min_duration(durations):
    min_ = min(durations)
    return min_


def get_max_duration(durations):
    max_ = max(durations)
    return max_


def get_len_courses(durations):
    min_ = get_min_duration(durations)
    max_ = get_max_duration(durations)
    maxes = []
    minis = []
    for index, lenght_course in enumerate(durations):
        if lenght_course == max_:
            maxes.append(index)
        elif lenght_course == min_:
            minis.append(index)
    return maxes, minis


# Соберите все названия самых коротких и самых длинных курсов
# Так как курсов с одной длительностью может быть больше одного,
# создайте список названий самых коротких (courses_min) и
# самых длинных (courses_max) курсов
def get_extremum_courses(maxes, minis, courses_list):
    courses_min = []
    courses_max = []
    for id in minis:
        # Допишите код, который берёт по id нужный курс из courses_list и
        # получает название курса из ключа "title"
        courses_min.append(courses_list[id]["title"])
    for id in maxes:
        # По аналогии допишите такой же код для курсов максимальной длительности
        courses_max.append(courses_list[id]["title"])
    return courses_max, courses_min


# Допишите конструкцию вывода результата. Можете использовать string.join()
# print(f"Самый короткий курс(ы): {', '.join(courses_min)} - {min} месяца(ев)")
# print(f"Самый длинный курс(ы): {', '.join(courses_max)} - {max} месяца(ев)")

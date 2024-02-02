import unittest

from task1 import (
    create_course_list,
    get_extremum_courses,
    get_len_courses,
    get_max_duration,
    get_min_duration,
)


class TestCourseFunctions(unittest.TestCase):
    def setUp(self):
        self.courses = [
            "Java-разработчик с нуля",
            "Fullstack-разработчик на Python",
            "Python-разработчик с нуля",
            "Frontend-разработчик с нуля",
        ]
        self.mentors = [
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
        self.durations = [14, 20, 12, 20]

        self.courses_list = create_course_list(
            self.courses, self.mentors, self.durations
        )
        self.min_duration = get_min_duration(self.durations)
        self.max_duration = get_max_duration(self.durations)
        self.maxes, self.minis = get_len_courses(self.durations)
        self.courses_max, self.courses_min = get_extremum_courses(
            self.maxes, self.minis, self.courses_list
        )

    def test_create_course_list(self):
        self.assertEqual(len(self.courses_list), 4)
        # add more specific checks on the course list here

    def test_get_min_duration(self):
        self.assertEqual(self.min_duration, 12)

    def test_get_max_duration(self):
        self.assertEqual(self.max_duration, 20)

    def test_get_extremum_courses(self):
        self.assertEqual(
            self.courses_max,
            ["Fullstack-разработчик на Python", "Frontend-разработчик с нуля"],
        )
        self.assertEqual(self.courses_min, ["Python-разработчик с нуля"])


if __name__ == "__main__":
    unittest.main()

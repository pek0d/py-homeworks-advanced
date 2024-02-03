import unittest

from task3 import get_all_list, get_all_names, get_unique_names


class TestMentorsFunctions(unittest.TestCase):
    def test_get_all_list(self):
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
        expected_result = [
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

        result = get_all_list(mentors)
        self.assertEqual(result, expected_result)

    def test_get_all_names(self):
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

        result = get_all_names(all_list)
        expected_result = [
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
        self.assertEqual(result, expected_result)

    def test_get_unique_names(self):
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
        result = get_unique_names(all_names_list)
        expected_result = (
            "Александр, Анна, Владимир, Дмитрий, Евгений, Иван, Олег, Филипп, Эдгар"
        )
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

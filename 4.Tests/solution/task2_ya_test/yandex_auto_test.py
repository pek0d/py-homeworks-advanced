import unittest

import pysnooper
import requests
from settings import token


class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.folder_url = f"{self.base_url}/resources"
        self.headers = {"Authorization": token}

    @pysnooper.snoop()
    def test_create_folder_success(self):
        folder_name = "TestFolder"
        create_folder_url = f"{self.folder_url}?path={folder_name}"

        response = requests.put(create_folder_url, headers=self.headers)

        self.assertEqual(response.status_code, 201)

    def test_create_folder_failure_no_permission(self):
        folder_name = "ProtectedFolder"
        create_folder_url = f"{self.folder_url}?path={folder_name}"

        response = requests.put(create_folder_url, headers=self.headers)

        self.assertNotEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()  # Задача №2 Автотест API Яндекса

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

        # Make a POST request to create a folder
        response = requests.put(create_folder_url, headers=self.headers)

        # Assert that the response code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Optional: Assert that the folder appears in the list of files
        # You can make a separate GET request to the folder URL and verify its presence

    def test_create_folder_failure_invalid_path(self):
        invalid_folder_name = "InvalidPath**"
        create_folder_url = f"{self.folder_url}?path=/app/{invalid_folder_name}"

        # Make a POST request with an invalid folder name
        response = requests.put(create_folder_url, headers=self.headers)

        # Assert that the response code is not 201 (Created)
        self.assertNotEqual(response.status_code, 201)

    def test_create_folder_failure_no_permission(self):
        folder_name = "ProtectedFolder"
        create_folder_url = f"{self.folder_url}?path=/app/{folder_name}"

        # Make a POST request to create a folder in a location without permission
        response = requests.put(create_folder_url, headers=self.headers)

        # Assert that the response code is not 201 (Created)
        self.assertNotEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()  # Задача №2 Автотест API Яндекса

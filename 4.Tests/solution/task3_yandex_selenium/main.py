import time
import unittest

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class TestYandexAuth(unittest.TestCase):
    def setUp(self):
        path = ChromeDriverManager().install()
        # browser_service = Service(executable_path=path)
        # browser = Chrome(service=browser_service)
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://passport.yandex.ru/auth/")

    def test_login_success(self):
        login = self.driver.find_element_by_id("passp-field-login")
        login.send_keys("your_username")
        login.send_keys(Keys.RETURN)

        time.sleep(2)

        password = self.driver.find_element_by_id("passp-field-passwd")
        password.send_keys("your_password")
        password.send_keys(Keys.RETURN)

        time.sleep(5)
        current_url = self.driver.current_url
        self.assertEqual(current_url, "https://mail.yandex.ru/")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from webdrivermanager import GeckoDriverManager

class TestDjangoApp(unittest.TestCase):
    def setUp(self):
        # Use GeckoDriverManager to automatically download and manage GeckoDriver
        GeckoDriverManager().install()
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://localhost:8000/")
        self.assertIn("Home Page", self.driver.title)

    def test_login(self):
        self.driver.get("http://localhost:8000/login/")
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")
        username_input.send_keys("testuser")
        password_input.send_keys("testpassword")
        submit_button.click()
        self.assertEqual(self.driver.current_url, "http://localhost:8000/")

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class TestDjangoApp(unittest.TestCase):
    def setUp(self):
        # Set up WebDriver with GeckoDriver managed by GeckoDriverManager
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def tearDown(self):
        # Clean up after each test
        self.driver.quit()

    def test_home_page(self):
        # Example test case
        self.driver.get("http://localhost:8000/")
        self.assertIn("Home Page", self.driver.title)

    def test_login(self):
        # Example test case
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

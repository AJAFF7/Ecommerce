import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestDjangoApp(unittest.TestCase):
    def setUp(self):
        # Set up WebDriver (e.g., ChromeDriver)
        self.driver = webdriver.Chrome()  # Or specify path to chromedriver executable

    def tearDown(self):
        # Clean up after each test
        self.driver.quit()

    def test_home_page(self):
        # Open the home page
        self.driver.get("http://localhost:8000/")  # Replace with your Django server URL

        # Example: Assert that the home page title is correct
        self.assertIn("Home Page", self.driver.title)

    def test_login(self):
        # Open the login page
        self.driver.get("http://localhost:8000/login/")  # Replace with your login URL

        # Example: Fill in login form and submit
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_xpath("//input[@type='submit']")

        username_input.send_keys("testuser")
        password_input.send_keys("testpassword")
        submit_button.click()

        # Example: Assert that after logging in, user is redirected to the home page
        self.assertEqual(self.driver.current_url, "http://localhost:8000/")

if __name__ == "__main__":
    unittest.main()

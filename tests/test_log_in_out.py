# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from webdriver_manager.firefox import GeckoDriverManager
# import unittest

# class TestDjangoApp(unittest.TestCase):
#     def setUp(self):
#         service = Service(executable_path=GeckoDriverManager().install())
#         options = webdriver.FirefoxOptions()
#         options.headless = True  # Run Firefox in headless mode
#         self.driver = webdriver.Firefox(service=service, options=options)

#     def tearDown(self):
#         self.driver.quit()

#     def test_home_page(self):
#         self.driver.get('http://localhost:8000')
#         self.assertIn("Welcome", self.driver.title)

#     def test_login(self):
#         self.driver.get('http://localhost:8000/login/')
#         username = self.driver.find_element_by_name('username')
#         password = self.driver.find_element_by_name('password')
#         username.send_keys('admin')
#         password.send_keys('password')
#         self.driver.find_element_by_name('submit').click()
#         self.assertIn("Dashboard", self.driver.title)

# if __name__ == '__main__':
#     unittest.main()

import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost"
    
    def test(self):
        self.step_1_login()
        self.step_2_search()

    def step_1_login(self):
        self.browser.get(self.url + "/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")

        self.browser.find_element(By.TAG_NAME, "button").click()

    def step_2_search(self):
        search_input = self.browser.find_element(By.ID, "employee_filter").find_element(By.TAG_NAME, "input")
        search_input.send_keys("doe") # trying get employee contains "doe" (John Does)

        expected_result = 'John Does'
        actual_result = self.browser.find_element(By.CLASS_NAME, "odd").find_elements(By.TAG_NAME, "td")[1].text # odd = class for first row in table. expected only 1 value found

        self.assertTrue(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
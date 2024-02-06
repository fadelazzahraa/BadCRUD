import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.FirefoxOptions()
        option.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost:8068/badcrud"
    
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
        search_input.send_keys(Keys.ENTER)

        expected_result = 'John Does'
        actual_result = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{expected_result}')]")

        self.assertTrue(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
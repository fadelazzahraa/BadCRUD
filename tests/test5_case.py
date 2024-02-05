import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.FirefoxOptions()
        # option.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        

    def test_5_login_with_sql_injection_attack(self):
        self.browser.get("http://localhost:8068/badcrud/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        # wrong cred
        username_input.send_keys('admin"#') # attack based on sql query that use double quote
        password_input.send_keys("password")

        self.browser.find_element(By.TAG_NAME, "button").click()

        self.browser.implicitly_wait(2)

        expected_result = 'Halo, admin"#'
        actual_result = self.browser.find_element(By.TAG_NAME, "h2").text

        self.assertTrue(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
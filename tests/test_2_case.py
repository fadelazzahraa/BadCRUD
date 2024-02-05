import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.FirefoxOptions()
        self.browser = webdriver.Firefox(options=option)
        option.add_argument('--headless')
        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost"
        

    def test_2_login_with_wrong_password_credentials(self):
        self.browser.get(self.url + "/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        # wrong password cred
        username_input.send_keys("admin")
        password_input.send_keys("password")

        self.browser.find_element(By.TAG_NAME, "button").click()

        self.browser.implicitly_wait(2)

        expected_result = "Wrong usename or password"
        actual_result = self.browser.find_element(By.CLASS_NAME, "checkbox").find_element(By.TAG_NAME, "label").text

        self.assertTrue(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
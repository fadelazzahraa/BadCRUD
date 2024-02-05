import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        option = webdriver.FirefoxOptions()
        # option.add_argument('--headless')
        self.browser = webdriver.Firefox(options=option)
        

    def test_4_login_with_wrong_credentials(self):
        self.browser.get("http://localhost:8068/badcrud/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        # wrong cred
        username_input.send_keys("user")
        password_input.send_keys("nimda666!")

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
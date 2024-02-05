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
        

    def test_1_login(self):
        self.browser.get(self.url + "/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")

        self.browser.find_element(By.TAG_NAME, "button").click()

    def test_2_go_to_create_contact(self):
        self.browser.find_element(By.CLASS_NAME, "create-contact").click()

    def test_3_fill_form_and_submit(self):
        self.browser.find_element(By.ID, "name").send_keys("Fadel Azzahra")
        self.browser.find_element(By.ID, "email").send_keys("fadel@mail.com")
        self.browser.find_element(By.ID, "phone").send_keys("01234567890")
        self.browser.find_element(By.ID, "title").send_keys("Tester")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[5]").click()

    def test_4_search_new_value(self):
        search_input = self.browser.find_element(By.ID, "employee_filter").find_element(By.TAG_NAME, "input")
        search_input.send_keys("Fadel Azzahra") # get new employee contains "Fadel Azzahra"

        expected_result = 'Fadel Azzahra'
        actual_result = self.browser.find_element(By.CLASS_NAME, "odd").find_elements(By.TAG_NAME, "td")[1].text # odd = class for first row in table. expected only 1 value found

        self.assertTrue(expected_result, actual_result)
    
    def test_5_clear_mess(self):
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[7]/a[2]").click()
        self.browser.switch_to.alert.accept()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
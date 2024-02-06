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
            self.url = "http://localhost"
    
    def test(self):
        self.step_1_login()
        self.step_2_go_to_create_contact()
        self.step_3_fill_form_and_submit()
        self.step_4_search_new_value()
        self.step_5_fill_form_to_edit_and_submit()
        self.step_6_search_edited_value()
        self.step_7_clear_mess()

    def step_1_login(self):
        self.browser.get(self.url + "/login.php")

        username_input = self.browser.find_element(By.ID, "inputUsername")
        password_input = self.browser.find_element(By.ID, "inputPassword")
        username_input.send_keys("admin")
        password_input.send_keys("nimda666!")

        self.browser.find_element(By.TAG_NAME, "button").click()

    def step_2_go_to_create_contact(self):
        self.browser.find_element(By.CLASS_NAME, "create-contact").click()

    def step_3_fill_form_and_submit(self):
        self.browser.find_element(By.ID, "name").send_keys("Account to Edit")
        self.browser.find_element(By.ID, "email").send_keys("edit@mail.com")
        self.browser.find_element(By.ID, "phone").send_keys("01234567890")
        self.browser.find_element(By.ID, "title").send_keys("Tester")
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[5]").click()

    def step_4_search_new_value(self):
        search_input = self.browser.find_element(By.ID, "employee_filter").find_element(By.TAG_NAME, "input")
        search_input.send_keys("Account to Edit") # get account to edit
        search_input.send_keys(Keys.ENTER)

        expected_result = 'Account to Edit'
        actual_result = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{expected_result}')]")
        self.assertTrue(expected_result, actual_result)

        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[7]/a[1]").click()

    def step_5_fill_form_to_edit_and_submit(self):
        self.browser.find_element(By.ID, "name").clear()
        self.browser.find_element(By.ID, "name").send_keys("Account is Edited")
        self.browser.find_element(By.ID, "email").clear()
        self.browser.find_element(By.ID, "email").send_keys("edited@mail.com")
        self.browser.find_element(By.ID, "phone").clear()
        self.browser.find_element(By.ID, "phone").send_keys("1111111111")
        self.browser.find_element(By.ID, "title").clear()
        self.browser.find_element(By.ID, "title").send_keys("Tester")
        
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/form/input[5]").click()

    def step_6_search_edited_value(self):
        search_input = self.browser.find_element(By.ID, "employee_filter").find_element(By.TAG_NAME, "input")
        search_input.send_keys("Account is Edited") # get edited account
        search_input.send_keys(Keys.ENTER)

        expected_result = "Account is Edited"
        actual_result = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{expected_result}')]")

        self.assertTrue(expected_result, actual_result)
    
    def step_7_clear_mess(self):
        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr/td[7]/a[2]").click()

        self.browser.switch_to.alert.accept()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 
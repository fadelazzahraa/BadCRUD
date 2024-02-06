from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def get_session():
    option = webdriver.FirefoxOptions()
    option.add_argument('--headless')
    driver = webdriver.Firefox(options=option)

    try:
        try:
            url = os.environ['URL']
        except:
            url = "http://localhost/"

        driver.get(url)
        driver.find_element(By.NAME, "username").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("nimda666!")
        driver.find_element(By.XPATH, "/html/body/form/button").click()


        session_cookie = driver.get_cookie("PHPSESSID")["value"]
        print(f"Sesi Login: {session_cookie}")


        with open("session_file.txt", "w") as file:
            file.write(session_cookie)

    finally:
        driver.quit()

if __name__ == "__main__":
    get_session()

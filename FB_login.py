import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\programming\\webdrivers\\chromedriver.exe")
        self.driver.get("https://facebook.com")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        fbUserName = "*************"
        fbPwd = "*******"

        emailId = "email"
        pwdId = "pass"
        loginBtnXpath = '//input[@value="Log In"]'
        fbLogoXpath = ''

        #emailEle = driver.find_element_by_name(emailId)
        #pwdEle = driver.find_element_by_name(pwdId)

        emailEle = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_name(emailId))
        pwdEle = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_name(pwdId))
        loginBtnEle = WebDriverWait(driver,10).until(lambda  driver: driver.find_element_by_xpath(loginBtnXpath))

        emailEle.send_keys(fbUserName)
        pwdEle.send_keys(fbPwd)
        loginBtnEle.click()
        print(driver.title)
        self.assertIn("Facebook – log in or sign up ", driver.title)
        #assert "Facebook – log in or sign up " in driver.title

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



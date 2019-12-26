import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\\programming\\webdrivers\\chromedriver.exe")

    def test_google_search(self):
        driver = self.driver
        driver.get("http://google.com")
        self.assertIn("Google",driver.title)
        ele = driver.find_element_by_name("q")
        ele.clear()
        ele.send_keys("python automation")
        ele.send_keys(Keys.RETURN)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()





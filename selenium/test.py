
import unittest
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import xmlrunner

class Test(unittest.TestCase):

        def test_emptyform(self):
            # Setup
            options = Options()
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(options=options)

            # Get the home page
            driver.get("http://127.0.0.1:5000/")

            # Finds button using its xpath
            search_field = driver.find_element(By.XPATH, "//input[@id='search']")
            search_field.submit()

            # Get error message
            message=driver.find_element(By.XPATH, "//h1").text

            # Test
            self.assertTrue(message=='unsucessful login')

        def test_xxs(self):
            # Setup
            options = Options()
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(options=options)

            # Get the registration page
            driver.get("http://127.0.0.1:5000/")

            # Get the form element inputs
            search_field = driver.find_element(By.XPATH, "//input[@id='search']")  
            search_field.send_keys('<script> alert("1");</script>')
            search_field.submit()

            # Get error message
            message=driver.find_element(By.XPATH, "//h1").text

            # Test
            self.assertTrue(message=='unsucessful login')

        def test_normalinput(self):
            # Setup
            options = Options()
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome(options=options)

            # Get the registration page
            driver.get("http://127.0.0.1:5000/")

            # Get the form element inputs
            search_field = driver.find_element(By.XPATH, "//input[@id='search']")  
            search_field.send_keys('hi')
            search_field.submit()

            # Get error message
            message=driver.find_element(By.XPATH, "//h1").text

            # Test
            self.assertTrue(message=='Search Result: hi')


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False)



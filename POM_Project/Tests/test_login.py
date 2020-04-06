import unittest
from selenium import webdriver
import time
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))  # ".." shows how many levels
from POM_Project.Pages.loginPage import LoginPage
from POM_Project.Pages.homePage import HomePage
import HtmlTestRunner
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.common.by import By


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome(
            executable_path="/Users/tatiana/Desktop/PROJECTS/UnitTest_POM_2020_03_28/Drivers/chromedriver")
        '''Implicit wait is applicable to each element on web page. It's checking and  
        waiting for existence of the element'''
        cls.browser.implicitly_wait(5)
        cls.browser.maximize_window()

    def test_01_login_valid(self):
        browser = self.browser

        browser.get("https://opensource-demo.orangehrmlive.com/")

        page = LoginPage(browser)
        page.enter_username("Admin")
        page.enter_password("admin123")
        page.click_login_button()

        '''Change to explicit wait later'''
        time.sleep(2)
        '''explicit wait is checking if element has proper condition:
        present, clickable, wait til element gets enabled,
         waut till text present etc.'''
        # wait = WebDriverWait(browser, 10)
        # dashboard = wait.until(ES.element_is_displayed((By.ID, "menu_dashboard_index")))
        # assert dashboard == "True"

        homepage = HomePage(browser)
        homepage.click_welcome_admin()
        homepage.click_logout()

        time.sleep(5)

    def test_02_login_invalid(self):
        browser = self.browser

        browser.get("https://opensource-demo.orangehrmlive.com/")

        page = LoginPage(browser)
        page.enter_username("Admin1")
        page.enter_password("admin123")
        page.click_login_button()
        time.sleep(2)
        message = page.check_span_message_text()
        self.assertTrue(message, "Invalid credentials")

        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        print("\nTest was COMPLETED!!!")
        cls.browser.quit()



if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output="/Users/tatiana/Desktop/PROJECTS/UnitTest_POM_2020_03_28/Reports"))

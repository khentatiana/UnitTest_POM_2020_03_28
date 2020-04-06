from POM_Project.Locators.locators import Locators

class HomePage():
    def __init__(self, browser):
        self.browser = browser

    # after moving locators to separate file, do import "from POM_Project.Locators.locators import Locators"
    # modify locators
        self.welcome_admin_xpath = Locators.welcome_admin_xpath
        self.logout_xpath = Locators.logout_xpath


    # If you want to keep locators separately, then move them to locators.py
    # self.welcome_admin_xpath = "//a[@id='welcome']"
    # self.logout_xpath = "//a[contains(text(),'Logout')]"

    def click_welcome_admin(self):
        self.browser.find_element_by_xpath(self.welcome_admin_xpath).click()

    def click_logout(self):
        self.browser.find_element_by_xpath(self.logout_xpath).click()

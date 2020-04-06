from POM_Project.Locators.locators import Locators

class LoginPage():
    # create a constructor. This constructor will be called every time when we create the object from
    # this class LoginPage()
    def __init__(self, browser):
        # create browser instance
        self.browser = browser

        # after moving locators to separate file, do import "from POM_Project.Locators.locators import Locators"
        # modify locators
        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.span_message_id = Locators.spanMessage_id

        # If you want to keep locators separately, then move them to locators.py

        # self.username_textbox_id = "txtUsername"
        # self.password_textbox_id = "txtPassword"
        # self.login_button_id = "btnLogin"

    def enter_username(self, username):
        self.browser.find_element_by_id(self.username_textbox_id).clear()
        self.browser.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element_by_id(self.password_textbox_id).clear()
        self.browser.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_button(self):
        self.browser.find_element_by_id(self.login_button_id).click()

    def check_span_message_text(self):
        message = self.browser.find_element_by_id(self.span_message_id).text
        return message

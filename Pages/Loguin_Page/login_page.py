import time
from selenium.webdriver.common.by import By
from Utilities.UI.webdriver_actions.element_actions import Element_Actions
from Utilities.UI.webdriver_actions.elements_actions  import Elements_Actions
from Pages.base_page import Base_Page
from Pages.locator import Locator
from .login_page_elements import Login_Page_Elements
from Config.UI.config_path import page_path_configuration
from hamcrest import assert_that, equal_to

class Login_Page(Login_Page_Elements):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    url = page_path_configuration.get_url_page("DEV","loguin_page")

    def set_username(self, value):
        self.user_name.set_text(value)
        
    def set_pasword(self, value):
        self.password.set_text(value)
    
    def click_login(self):
        self.login_button.click()
    
    def get_error_message(self):
        return self.error_message.get_text()
import time
from selenium.webdriver.common.by import By
from Driverfactory.Actions.element_actions import BaseElement
from Pages.base_page import BasePage
from Pages.locator import Locator
from .login_page_elements import login_page_elements
from Config.UI.config_path import page_path_configuration
from hamcrest import assert_that, equal_to

class login_page(login_page_elements):
    
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
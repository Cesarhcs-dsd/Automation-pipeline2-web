from selenium.webdriver.common.by import By
from Driverfactory.Actions.element_actions import BaseElement
from Pages.base_page import BasePage
from Pages.locator import Locator

class login_page_elements(BasePage):
    def __init__(self, driver):
        self.driver = driver

    @property
    def user_name(self):
        locator = Locator(by=By.ID, value= 'exampleInputEmail1')
        return BaseElement(self.driver, locator)

    @property
    def password(self):
        locator = Locator(by=By.ID, value= 'exampleInputPassword1')
        return BaseElement(self.driver, locator)
    
    @property
    def login_button(self):
        locator = Locator(by=By.XPATH, value= "//*[@class='mat-button-wrapper']")
        return BaseElement(self.driver, locator)
    
    @property
    def error_message(self):
        locator = Locator(by=By.XPATH, value= "//*[@class='signInErrMsg ng-star-inserted']")
        return BaseElement(self.driver, locator)
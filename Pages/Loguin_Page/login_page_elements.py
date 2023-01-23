from selenium.webdriver.common.by import By
from Utilities.UI.webdriver_actions.element_actions import Element_Actions
from Utilities.UI.webdriver_actions.elements_actions  import Elements_Actions
from Pages.base_page import Base_Page
from Pages.locator import Locator

class Login_Page_Elements(Base_Page):
    def __init__(self, driver):
        self.driver = driver

    @property
    def user_name(self):
        locator = Locator(by=By.ID, value= 'exampleInputEmail1')
        return Element_Actions(self.driver, locator)

    @property
    def password(self):
        locator = Locator(by=By.ID, value= 'exampleInputPassword1')
        return Element_Actions(self.driver, locator)
    
    @property
    def login_button(self):
        locator = Locator(by=By.XPATH, value= "//*[@class='mat-button-wrapper']")
        return Element_Actions(self.driver, locator)
    
    @property
    def error_message(self):
        locator = Locator(by=By.XPATH, value= "//*[@class='signInErrMsg ng-star-inserted']")
        return Element_Actions(self.driver, locator)
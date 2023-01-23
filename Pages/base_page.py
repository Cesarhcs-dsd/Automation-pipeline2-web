from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .locator import Locator


class Base_Page():
    url = None

    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get(self.url)
    
    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url
        

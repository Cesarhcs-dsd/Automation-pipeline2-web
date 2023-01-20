from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None
        self.find()

    def find(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator=self.locator)
            )
            self.web_element = element
        except:
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(locator=self.locator)
            )
            self.web_element = element
        else:
            pass
        return None

    def set_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def click(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator=self.locator)
            )
            element.click()
        except:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(locator=self.locator)
            )
            element.click()
        return None

    def get_text(self):
        text = self.web_element.text
        return text

    def is_displayed(self):
        return EC.WebElement.is_displayed(self.web_element)

    def scroll_to(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.web_element).perform()

    def is_displayedr(self):
        return len(EC.WebElement.find_elements(self.web_element))


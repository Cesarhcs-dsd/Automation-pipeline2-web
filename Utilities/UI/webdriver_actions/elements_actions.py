from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select as select
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import pandas as pd


class Elements_Actions(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_elements = None
        self.find_elements()

    def find_elements(self):
        try:
            elements = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_any_elements_located(locator=self.locator)
            )
            self.web_elements = elements
        except:
            elements = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located(locator=self.locator)
            )
            self.web_elements = elements
        else:
            pass
        return None

    def get_texts(self):
        attribute = self.web_elements
        texts = []
        for sistema in attribute:
            texts.append(sistema.text)
        return texts

    def get_atribuites(self, atribute):
        atributes = []
        for sistema in self.web_elements:
            value = sistema.get_attribute(atribute)
            atributes.append(value)
        return atributes

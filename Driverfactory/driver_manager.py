from abc import abstractmethod
from contextlib import nullcontext
from pickle import NONE
from selenium import webdriver


class driver_manager():

    @abstractmethod
    def star_service():
        pass

    @abstractmethod
    def stop_service():
        pass

    @abstractmethod
    def create_driver():
        pass

    def quit_driver():
        if nullcontext != webdriver :
            webdriver.quit
            webdriver = nullcontext

    def get_driver():
        if nullcontext == webdriver :
            driver_manager.create_driver()
        return webdriver
from abc import abstractmethod
from contextlib import nullcontext
from pickle import NONE
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Driver_Manager():
    
    @abstractmethod
    def create_driver():
        pass
    
    @abstractmethod
    def get_chrome_options():
        pass
    
    @abstractmethod
    def get_chrome_service():
        pass
    
    def star_service():
        Service.start

    def stop_service():
        if Service != None and Service.assert_process_still_running:
            Service.stop

    def quit_driver(driver):
        if nullcontext != driver :
            driver.close()
            driver.quit()
            driver = nullcontext
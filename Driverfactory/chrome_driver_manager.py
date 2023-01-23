from Driverfactory.driver_manager import Driver_Manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Chrome_Driver_Manager(Driver_Manager):


    def create_driver():
        driver = webdriver.Chrome(
            service=Chrome_Driver_Manager.get_chrome_service() ,
            chrome_options= Chrome_Driver_Manager.get_chrome_options() 
        )
        driver.implicitly_wait(10)
        return driver
    
    def get_chrome_options() :
        chrome_options = webdriver.ChromeOptions()
        return chrome_options
    
    def get_chrome_service() :
        service=Service(ChromeDriverManager().install())
        return service

    
   


from Driverfactory.driver_manager import driver_manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class chrome_driver_manager(driver_manager):

    def stop_service():
        if Service != None and Service.assert_process_still_running:
            Service.stop


    def create_driver():
        chrome_options = webdriver.ChromeOptions()
        ##chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            chrome_options=chrome_options
        )
        driver.implicitly_wait(10)
        return driver
   


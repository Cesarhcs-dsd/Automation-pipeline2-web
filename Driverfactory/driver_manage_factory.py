from Driverfactory.chrome_driver_manager import chrome_driver_manager

class driver_manage_factory ():

    def driver_manager_browsers(driver):
        match driver:
            case "chrome":
                driverweb = chrome_driver_manager.create_driver()
                return driverweb
            case _:
                driverweb = chrome_driver_manager.create_driver()
                return driverweb

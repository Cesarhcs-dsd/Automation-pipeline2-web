from Driverfactory.chrome_driver_manager import Chrome_Driver_Manager

class driver_manage_factory ():

    def driver_manager_browsers(driver):
        match driver:
            case "chrome":
                driverweb = Chrome_Driver_Manager
                return driverweb
            case _:
                driverweb = Chrome_Driver_Manager
                return driverweb

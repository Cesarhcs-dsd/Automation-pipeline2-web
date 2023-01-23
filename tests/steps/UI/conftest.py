import time
from pytest import fixture,yield_fixture
from selenium import webdriver
from Driverfactory.driver_manage_factory import driver_manage_factory
from Pages.Loguin_Page.login_page import Login_Page


def pytest_addoption(parser):
    parser.addoption(
        "--browser", 
        action="store",
        default='Chrome',
        help="Wich browser it's going to use"
    ) 


@fixture(scope='session')
def browser(request):
    return request.config.getoption("--browser")


@fixture(scope='session')
def browserdri(browser):
    selenium_manager = driver_manage_factory.driver_manager_browsers(browser)
    driver = selenium_manager.create_driver()
    yield driver
    #driver.quit()
    #driver.close()
    selenium_manager.quit_driver(driver)
    selenium_manager.stop_service()
    
@fixture(scope='session')
def page(browserdri):
    return Login_Page(browserdri)

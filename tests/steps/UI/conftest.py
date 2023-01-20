import time
from pytest import fixture,yield_fixture
from selenium import webdriver
from Driverfactory.driver_manage_factory import driver_manage_factory
from Pages.Loguin_Page.login_page import login_page


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
    drvr = driver_manage_factory.driver_manager_browsers(browser)
    yield drvr
    drvr.quit()
    
@fixture(scope='session')
def page(browserdri):
    return login_page(browserdri)

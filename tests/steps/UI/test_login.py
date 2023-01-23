from pytest import Parser, Session, fixture
from hamcrest import assert_that, equal_to
import pytest
from pytest_bdd import given, when, then, scenario, scenarios, parsers
from Pages.Loguin_Page.login_page import Login_Page
from Utilities.loggin.Mylogger import MyLogger
from Utilities.loggin.loggin import log


scenarios('UI/login.feature')


@given(parsers.parse('the user "{email}" is trying to loguin with the password "{password}"'))
def fill_password_and_email(browserdri,page,email, password):
    page.go_to()
    page.set_username(email)
    page.set_pasword(password)


@when('the user clicks on the login button')
def click_on_login_button(browserdri, page):
    page.click_login()     

    
@log(my_logger=MyLogger())
@then('the system shoudl displays an error message')
def verify_error_message(browserdri, page):
    assert_that(page.get_error_message(), equal_to("Wrong username or password. Username and password are case sensitive."))
        
        

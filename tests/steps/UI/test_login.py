from pytest import Parser, Session, fixture
from hamcrest import assert_that, equal_to
import pytest
from pytest_bdd import given, when, then, scenario, scenarios, parsers
from Pages.Loguin_Page.login_page import login_page
from Utilities.loggin.Mylogger import MyLogger
from Utilities.loggin.loggin import log


scenarios('UI/login.feature')


@given(parsers.parse('the user "{email}" is trying to loguin with the password "{password}"'))
def fill_password_and_email(browserdri,email, password):
    login_page(browserdri).go_to()
    login_page(browserdri).set_username(email)
    login_page(browserdri).set_pasword(password)


@when('the user clicks on the login button')
def click_on_login_button(browserdri):
    login_page(browserdri).click_login()     

    
@log(my_logger=MyLogger())
@then('the system shoudl displays an error message')
def verify_error_message(browserdri):
    assert_that(login_page(browserdri).get_error_message(), equal_to("Wrong username or password. Username and password are case sensitive."))
        
        

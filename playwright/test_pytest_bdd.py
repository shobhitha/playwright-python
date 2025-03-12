import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from playwrightpytestpython.conftest import user_credentials
from playwrightpytestpython.pageObjects.login import LoginPage
from playwrightpytestpython.utils.apiBaseFramework import APIUtilsFramework

scenarios('../features/orderTransaction.feature')
@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('Place the item order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["user_email"] = username
    user_credentials["password"] = password

    api_utils = APIUtilsFramework()
    order_Id = api_utils.create_order(playwright, user_credentials)
    shared_data['order_Id'] = order_Id

@given('the user is on landing page')
def user_landing_page(browserInstance, shared_data):
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    shared_data['login_page'] = login_page

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(username, password)
    shared_data['dashboard_page'] = dashboard_page

@when('navigate to Orders page')
def navigate_to_order_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.select_orders_link()
    shared_data['order_history_page'] = order_history_page

@when('Select the orderID')
def select_order(shared_data):
    order_history_page = shared_data['order_history_page']
    order_Id = shared_data['order_Id']
    order_details_page = order_history_page.select_order(order_Id)
    shared_data['order_details_page'] = order_details_page

@then('Order message is successfully displayed')
def verify_success_message(shared_data):
    order_details_page = shared_data['order_details_page']
    order_details_page.verify_order_page()




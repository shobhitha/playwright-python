import json
from os import login_tty

import pytest
from playwright.sync_api import Playwright, expect

from playwrightpytestpython.pageObjects.dashboard import DashboardPage
from playwrightpytestpython.pageObjects.login import LoginPage
from playwrightpytestpython.utils.apiBase import APIUtils
from playwrightpytestpython.utils.apiBaseFramework import APIUtilsFramework

#access data
with open('../data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserInstance, user_credentials):
    user_email = user_credentials["user_email"]
    user_password = user_credentials["password"]
#create order
    api_utils = APIUtilsFramework()
    order_Id = api_utils.create_order(playwright,user_credentials)
#login
    login_page = LoginPage(browserInstance)
    login_page.navigate()
    dashboard_page = login_page.login(user_email,user_password)
#DashboardPage
    order_history_page = dashboard_page.select_orders_link()
    # order history page and check order is present
    order_details_page = order_history_page.select_order(order_Id)
    order_details_page.verify_order_page()


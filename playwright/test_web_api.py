from os import login_tty

from playwright.sync_api import Playwright, expect

from playwrightpytestpython.utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

#create order
    api_utils = APIUtils()
    order_Id = api_utils.create_order(playwright)

#login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

#order history page and check order is present
    page.get_by_role("button", name = "ORDERS").click()
    row = page.locator("tr").filter(has_text=order_Id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()

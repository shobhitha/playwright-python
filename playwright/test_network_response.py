from datetime import time


from playwright.sync_api import Page, expect

import pytest

fake_payload_order_response = {"data":[],"message":"No Orders"}
def intercept_response(route):
    route.fulfill(
        json=fake_payload_order_response
    )

@pytest.mark.smoke
def test_network(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    #time.sleep(5)
    expect(page.locator(".mt-4 ")).to_have_text("You have No Orders to show at this time. Please Visit Back Us")
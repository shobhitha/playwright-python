from datetime import time

from playwright.sync_api import Playwright, Page, expect

"""def test_firefoxBrowser(playwright: Playwright):
    firefoxBrowser = playwright.firefox.launch(headless=False)
    context = firefoxBrowser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise")"""



"""def test_playwrightBasics(playwright:Playwright):
    chrome_browser = playwright.chromium.launch(headless=False)
    context = chrome_browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")"""



def test_coreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learnin")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()












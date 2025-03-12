from playwright.sync_api import sync_playwright, Page


def handle_dialog(dialog):
    print(dialog.message())
    dialog.accept()



def test_UIValidationDynamicScript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password").fill("learning")
    #page.on("dialog", lambda dialog: dialog.accept())
    #page.locator("input[value='user']").check()
    #page.evaluate("alert('1')")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    iphone_product = page.locator("app-card").filter(has_text="iphone X")
    iphone_product.get_by_role("button",).click()
    nokia_product = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button", ).click()


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")

    with page.expect_popup() as newPage_info:

        page.locator(".blinkingText").click()
        child_page = newPage_info.value
        text = child_page.locator(".red").text_content()
        print(text)
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"









from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button",name= "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


    #AlertBox
    page.on("dialog", lambda dialog : dialog.accept())
    page.get_by_role("button", name = "Confirm").click()


    #Frame
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name = "All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

    #check the price of the rice is 37

    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    price_colval = 0

    for i in range(page.locator("th").count()):

        if page.locator("th").nth(i).filter(has_text="Price").count()>0:
            price_colval = i
            print(f"Price column value is {price_colval}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(price_colval)).to_have_text("37")









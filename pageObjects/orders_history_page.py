from playwrightpytestpython.pageObjects.order_details_page import OrderDetailsPage


class OrderHistoryPage:

    def __init__(self,page):
        self.page = page

    def select_order(self, order_Id):
        row = self.page.locator("tr").filter(has_text=order_Id)
        row.get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page
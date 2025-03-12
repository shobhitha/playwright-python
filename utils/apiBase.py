from playwright.sync_api import Playwright
from pytest_base_url.plugin import base_url

orders_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}
login_payload = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"}
class APIUtils:

    def get_token(self,playwright:Playwright):
        api_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_new_context.post("/api/ecom/auth/login",
                                        data =login_payload)

        print(response.json())
        response_body = response.json()
        return response_body["token"]



    def create_order(self,playwright:Playwright):

        token = self.get_token(playwright)
        api_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_new_context.post("/api/ecom/order/create-order",
                             data = orders_payload,
                             headers = {"Authorization": token,
                                         "Content-Type": "application/json"}
                            )
        print(response.json())
        response_body = response.json()
        order_Id = response_body["orders"][0]
        return order_Id



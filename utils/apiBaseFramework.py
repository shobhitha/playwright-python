from playwright.sync_api import Playwright
from pytest_base_url.plugin import base_url

orders_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}
#login_payload = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"}
class APIUtilsFramework:

    def get_token(self,playwright:Playwright, user_credentials):
        user_email = user_credentials["user_email"]
        user_password = user_credentials["password"]

        api_new_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_new_context.post("/api/ecom/auth/login",
                                        data = {"userEmail": user_email, "userPassword": user_password})

        print(response.json())
        response_body = response.json()
        return response_body["token"]



    def create_order(self,playwright:Playwright, user_credentials):

        token = self.get_token(playwright, user_credentials)
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



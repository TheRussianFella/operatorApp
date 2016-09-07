import requests
import json

class WebClient:

    def __init__(self, host):
        self.host = host

    def getOrders(self):
        response = requests.get(self.host + "/api/get_orders")

        if response.status_code != 200:
            print("Error:" + str(response.status_code))
            return

        orders = json.loads(response.text)

        return orders

    def getPic(self, url):
        response = requests.get(self.host + url)
        return response

    def reportComplition(self, id):
        requests.post(self.host + "/order_set_completed", id)

import requests
import json

class WebClient:

    host = ""

    def __init__(self, host):
        self.host = host

    def getOrders(self):
        response = requests.get(self.host + "/api/get_orders")

        assert response.status_code == 200

        orders = json.loads(response.text)

        return orders

    #def getPics():
        #response = requests.get(_host)

    def reportComplition(self, id):
        requests.post(_host + "/complete", "OK")

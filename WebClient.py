import requests


class WebClient:

    _host = ""

    def __init__(self, host):
        self._host = host

    def getOrders(self):
        response = requests.get(_host + "\orders")

        assert response.status_code == 200

        orders = response.json()

        return orders

    def reportComplition(self, id):
        requests.post(_host + "\report", "OK")

from locust import TaskSet, task


class MarketTaskSet(TaskSet):

    @task(10)
    def create_market(self):
        payload = {
            "date": "2023-10-25",
            "close": 120.5,
            "high": 125.0,
            "low": 115.0,
            "open": 118.0,
            "volume": 1500000,
            "stock_id": 1
        }
        response = self.client.post("/market/", json=payload)
        if response.status_code != 200:
            print(f"Failed to create market data: {response.status_code}, {response.text}")

    @task(20)
    def list_markets(self):
        response = self.client.get("/market/")
        if response.status_code != 200:
            print(f"Failed to get market data list: {response.status_code}, {response.text}")

    @task(3)
    def get_market_by_id(self):
        response = self.client.get("/market/1")
        if response.status_code != 200:
            print(f"Failed to get market by ID: {response.status_code}, {response.text}")

    @task(1)
    def update_market(self):
        payload = {
            "date": "2023-10-25",
            "close": 122.0,
            "high": 127.0,
            "low": 114.0,
            "open": 120.0,
            "volume": 1600000,
            "stock_id": 1
        }
        response = self.client.put("/market/1", json=payload)
        if response.status_code != 200:
            print(f"Failed to update market data: {response.status_code}, {response.text}")

    @task(-1)
    def delete_market(self):
        response = self.client.delete("/market/1")
        if response.status_code != 200:
            print(f"Failed to delete market data: {response.status_code}, {response.text}")

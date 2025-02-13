from locust import TaskSet, task


class StockTaskSet(TaskSet):

    @task(1)
    def create_stock(self):
        payload = {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Technology",
            "businessSummary": "Apple designs mobile communication and media devices."
        }
        response = self.client.post("/Stock/", json=payload)
        if response.status_code != 200:
            print(f"Failed to create stock: {response.status_code}, {response.text}")

    @task(2)
    def list_stocks(self):
        response = self.client.get("/Stock/")
        if response.status_code != 200:
            print(f"Failed to get stocks: {response.status_code}, {response.text}")

    @task(1)
    def get_stock_by_ticker(self):
        response = self.client.get("/Stock/AAPL")
        if response.status_code != 200:
            print(f"Failed to get stock by ticker: {response.status_code}, {response.text}")

    @task(1)
    def update_stock(self):
        payload = {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "sector": "Consumer Electronics",
            "businessSummary": "Apple is a technology company creating premium products."
        }
        response = self.client.put("/Stock/AAPL", json=payload)
        if response.status_code != 200:
            print(f"Failed to update stock: {response.status_code}, {response.text}")

    @task(1)
    def delete_stock(self):
        response = self.client.delete("/Stock/AAPL")
        if response.status_code != 200:
            print(f"Failed to delete stock: {response.status_code}, {response.text}")

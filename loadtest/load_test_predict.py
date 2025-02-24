import random

from locust import HttpUser, TaskSet, task, between


class PredictTaskSet(TaskSet):

    @task(9)
    def predict_success(self):

        payload = {
            "Open": random.uniform(90.0, 130.00),
            "High": random.uniform(90.0, 130.00),
            "Low": random.uniform(90.0, 130.00),
            "Volume": random.uniform(250000000, 5250000000)
        }

        response = self.client.post("/predictions/", json=payload)

        if response.status_code != 200:
            print(f"Failed request: {response.status_code}, {response.text}")

    @task(1)
    def predict_invalid(self):

        payload = {
            "Open": -22.0
        }

        response = self.client.post("/predictions/", json=payload)

        if response.status_code == 200:
            print(f"Failed request: {response.status_code}, {response.text}")

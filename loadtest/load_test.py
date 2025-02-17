from locust import HttpUser, between

from load_test_market import MarketTaskSet
from load_test_predict import PredictTaskSet
from load_test_stock import StockTaskSet


class PredictTestUser(HttpUser):
    tasks = [PredictTaskSet]
    wait_time = between(1, 3)

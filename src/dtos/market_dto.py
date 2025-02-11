from pydantic import BaseModel
from datetime import date

# Ticker
class StockDTO(BaseModel):
    ticker: str
    name: str
    sector: str
    businessSummary: str

# Market
class MarketDTO(BaseModel):
    date: date
    close: float
    high: float
    low: float
    open: float
    volume: int
    stock_id: int
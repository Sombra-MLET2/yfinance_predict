from pydantic import BaseModel
from datetime import date

# Ticker
class TickerDTO(BaseModel):
    id: int | None = None
    ticker: str | None = None
    name: str | None = None
    sector: str | None = None
    businessSummary: str | None = None

class TickerDTOResponse(BaseModel):
    id: int | None = None
    ticker: str | None = None
    name: str | None = None
    sector: str | None = None
    businessSummary: str | None = None

# Market
class MarketDTO(BaseModel):
    id: int | None = None
    date: date 
    close: float | None = None
    high: float | None = None
    low: float | None = None
    ppen: float | None = None
    volume: float | None = None
    ticker_id: int

class MarketDTOResponse(BaseModel):
    id: int | None = None
    date: date 
    close: float | None = None
    high: float | None = None
    low: float | None = None
    ppen: float | None = None
    volume: float | None = None
    ticker: TickerDTO
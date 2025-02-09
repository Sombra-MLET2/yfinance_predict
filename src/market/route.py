from io import StringIO
from typing import List, Union, Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from src.infra.database import get_db

from src.repositories import market_repository
from src.repositories import ticker_repository

from src.dtos.market_dto import MarketDTO, MarketDTOResponse
from src.dtos.market_dto import TickerDTO, TickerDTOResponse

market_router = APIRouter(
    prefix="/merket",
    tags=["market"],
    responses={401: {"description": "Invalid credentials"},
               404: {"description": "Not found"},
               500: {"description": "Internal server error"}},
)

@market_router.get("/tickers",
                      summary="List all ickers",
                      response_model=List[TickerDTOResponse])
async def list_mushrooms(db_con: Session = Depends(get_db)):
    tickers = ticker_repository.find_all(db_con)
    return tickers
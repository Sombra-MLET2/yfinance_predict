from io import StringIO
from typing import List, Union, Annotated
from venv import logger

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from infra.database import get_db

from repositories.ticker_repository import TickerRepository

from dtos.market_dto import TickerDTO

ticker_router = APIRouter(
    prefix="/ticker",
    tags=["ticker"],
    responses={401: {"description": "Invalid credentials"},
               404: {"description": "Not found"},
               500: {"description": "Internal server error"}},
)

@ticker_router.post("/", response_model=TickerDTO)
def create_ticker(ticker: TickerDTO, db: Session = Depends(get_db)):
    logger.info("Recebida requisição para criar um ticker")
    repo = TickerRepository(db)
    return repo.create(ticker)

@ticker_router.get("/")
def get_tickers(db: Session = Depends(get_db)):
    logger.info("Recebida requisição para listar tickers")
    repo = TickerRepository(db)
    return repo.get_all()

@ticker_router.get("/{ticker_id}")
def get_ticker(ticker_id: int, db: Session = Depends(get_db)):
    logger.info("Recebida requisição para obter ticker {ticker_id}.")
    repo = TickerRepository(db)
    return repo.get_by_id(ticker_id)

@ticker_router.put("/{ticker_id}")
def update_ticker(ticker_id: int, ticker: TickerDTO, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para atualizar ticker {ticker_id}")
    repo = TickerRepository(db)
    updated_ticker = repo.update(ticker_id, ticker)
    if not updated_ticker:
        raise HTTPException(status_code=404, detail="Ticker não encontrado")
    return updated_ticker

@ticker_router.delete("/{ticker_id}")
def delete_ticker(ticker_id: int, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para deletar ticker {ticker_id}")
    repo = TickerRepository(db)
    if not repo.delete(ticker_id):
        raise HTTPException(status_code=404, detail="Ticker não encontrado")
    return {"message": "Ticker deletado com sucesso"}
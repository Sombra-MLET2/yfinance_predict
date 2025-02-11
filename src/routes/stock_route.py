from io import StringIO
from typing import List, Union, Annotated
from venv import logger

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from infra.database import get_db

from repositories.stock_repository import StockRepository

from dtos.market_dto import StockDTO

stock_router = APIRouter(
    prefix="/Stock",
    tags=["stock"],
    responses={401: {"description": "Invalid credentials"},
               404: {"description": "Not found"},
               500: {"description": "Internal server error"}},
)

@stock_router.post("/", summary="Create stocks."
                   , response_model=StockDTO)
def create_ticker(ticker: StockDTO, db: Session = Depends(get_db)):
    logger.info("Recebida requisição para criar um ticker")
    repo = StockRepository(db)
    return repo.create(ticker)

@stock_router.get("/", summary="List all stocks.")
def get_tickers(db: Session = Depends(get_db)):
    logger.info("Recebida requisição para listar tickers")
    repo = StockRepository(db)
    return repo.get_all()

@stock_router.get("/{ticker}", summary="Get stocks by ticker.")
def get_ticker(ticker: str, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para obter ticker {ticker}.")
    repo = StockRepository(db)
    return repo.get_by_ticker(ticker)

@stock_router.put("/{ticker}", summary="Update stock by ticker.")
def update_ticker(ticker: str, stock: StockDTO, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para atualizar ticker {ticker}")
    repo = StockRepository(db)
    updated_stock = repo.update(ticker, stock)
    if not updated_stock:
        raise HTTPException(status_code=404, detail="Ticker não encontrado")
    return updated_stock

@stock_router.delete("/{ticker}", summary="Delete stocks by ticker.")
def delete_ticker(ticker: str, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para deletar ticker {ticker}")
    repo = StockRepository(db)
    if not repo.delete(ticker):
        raise HTTPException(status_code=404, detail="Ticker não encontrado")
    return {"message": "Stock deletado com sucesso"}
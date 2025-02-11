from io import StringIO
from typing import List, Union, Annotated
from venv import logger

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response

from infra.database import get_db

from repositories.market_repository import MarketRepository

from dtos.market_dto import MarketDTO

market_router = APIRouter(
    prefix="/market",
    tags=["market"],
    responses={401: {"description": "Invalid credentials"},
               404: {"description": "Not found"},
               500: {"description": "Internal server error"}},
)

@market_router.post("/", response_model=MarketDTO)
def create_market(market: MarketDTO, db: Session = Depends(get_db)):
    logger.info("Recebida requisição para criar market data")
    repo = MarketRepository(db)
    return repo.create(market)

@market_router.get("/")
def get_markets(db: Session = Depends(get_db)):
    logger.info("Recebida requisição para listar market data")
    repo = MarketRepository(db)
    return repo.get_all()

@market_router.get("/{market_id}")
def get_markets(market_id: int, db: Session = Depends(get_db)):
    logger.info("Recebida requisição para obter market data {market_id}")
    repo = MarketRepository(db)
    return repo.get_by_id(market_id)

@market_router.put("/{market_id}")
def update_market(market_id: int, market: MarketDTO, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para atualizar market data {market_id}")
    repo = MarketRepository(db)
    updated_market = repo.update(market_id, market)
    if not updated_market:
        raise HTTPException(status_code=404, detail="Market data não encontrado")
    return updated_market

@market_router.delete("/{market_id}")
def delete_market(market_id: int, db: Session = Depends(get_db)):
    logger.info(f"Recebida requisição para atualizar market data {market_id}")
    repo = MarketRepository(db)
    if not repo.delete(market_id):
        raise HTTPException(status_code=404, detail="Market data não encontrado")
    return {"message": "Market data deletado com sucesso"}
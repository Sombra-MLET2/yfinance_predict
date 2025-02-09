import logging
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import or_

from src.dtos.market_dto import MarketDTO
from src.models.market import Market


def create_new(db: Session, dto: MarketDTO) -> Market:
    db_obj = Market(**dto.model_dump())

    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    except Exception as e:
        logging.error(f'Error while creating Market item: {e}')
        raise Exception(f'Error while creating Market item {dto.model_dump()}')


    return db_obj


def find_all(db: Session, dto: MarketDTO) -> List[Market]:
    return db.query(Market).order_by(Market.Market).all()

def find_by_ticker(db: Session, ticker_id: int) -> List[Market]:
    return db.query(Market).filter(Market.id == ticker_id).first()



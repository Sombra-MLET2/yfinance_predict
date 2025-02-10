import logging
from typing import List
from venv import logger

from sqlalchemy.orm import Session
from sqlalchemy import or_

from dtos.market_dto import MarketDTO
from models.market import Market


class MarketRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, market: MarketDTO):
        db_market = Market(**market.model_dump())
        self.db.add(db_market)
        self.db.commit()
        self.db.refresh(db_market)
        logger.info(
            f"Market data criado para ticker_id: {db_market.ticker_id}")
        return db_market

    def get_all(self):
        return self.db.query(Market).all()

    def get_by_id(self, market_id: int):
        return self.db.query(Market).filter(Market.id == market_id).first()

    def update(self, market_id: int, market_data: MarketDTO):
        market = self.get_by_id(market_id)
        if market:
            for key, value in market_data.model_dump().items():
                setattr(market, key, value)
            self.db.commit()
            self.db.refresh(market)
            logger.info(f"Market data atualizado: {market_id}")
            return market
        return None

    def delete(self, market_id: int):
        market = self.get_by_id(market_id)
        if market:
            self.db.delete(market)
            self.db.commit()
            logger.info(f"Market data deletado: {market_id}")
            return True
        return False

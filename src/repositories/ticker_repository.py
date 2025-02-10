import logging
from venv import logger

from sqlalchemy.orm import Session

from dtos.market_dto import TickerDTO
from models.ticker import Ticker

# Repositórios
class TickerRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, ticker: TickerDTO):
        db_ticker = Ticker(**ticker.model_dump())
        self.db.add(db_ticker)
        self.db.commit()
        self.db.refresh(db_ticker)
        logger.info(f"Ticker criado: {db_ticker.ticker}")
        return db_ticker

    def get_all(self):
        return self.db.query(Ticker).all()
    
    def get_by_id(self, ticker_id: int):
        return self.db.query(Ticker).filter(Ticker.id == ticker_id).first()
    
    def update(self, ticker_id: int, ticker_data: TickerDTO):
        ticker = self.get_by_id(ticker_id)
        if ticker:
            for key, value in ticker_data.model_dump().items():
                setattr(ticker, key, value)
            self.db.commit()
            self.db.refresh(ticker)
            logger.info(f"Ticker atualizado: {ticker_id}")
            return ticker
        return None
    
    def delete(self, ticker_id: int):
        ticker = self.get_by_id(ticker_id)
        if ticker:
            self.db.delete(ticker)
            self.db.commit()
            logger.info(f"Ticker deletado: {ticker_id}")
            return True
        return False

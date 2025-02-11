import logging
from venv import logger

from sqlalchemy.orm import Session

from dtos.market_dto import StockDTO
from models.stock import Stock

# Repositórios
class StockRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, stock: StockDTO):
        db_stock = Stock(**stock.model_dump())
        self.db.add(db_stock)
        self.db.commit()
        self.db.refresh(db_stock)
        logger.info(f"Stock criado: {db_stock.ticker}")
        return db_stock

    def get_all(self):
        return self.db.query(Stock).all()
    
    def get_by_ticker(self, ticker: str):
        return self.db.query(Stock).filter(Stock.ticker == ticker).first()

    def update(self, ticker: str, stock_data: StockDTO):
        db_stock = self.get_by_ticker(ticker)
        if db_stock:
            for key, value in stock_data.model_dump().items():
                setattr(db_stock, key, value)
            self.db.commit()
            self.db.refresh(db_stock)
            logger.info(f"Stock atualizado: {ticker}")
            return db_stock
        return None
    
    def delete(self, ticker: str):
        db_stock = self.get_by_ticker(ticker)
        if db_stock:
            self.db.delete(db_stock)
            self.db.commit()
            logger.info(f"Stock deletado: {ticker}")
            return True
        return False

import logging

from sqlalchemy.orm import Session

from src.dtos.market_dto import TickerDTO
from src.models.ticker import Ticker

def create_new(db: Session, dto: TickerDTO) -> Ticker:
    db_obj = Ticker(**dto.model_dump())

    try:
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    except Exception as e:
        logging.error(f'Error while creating Ticker item: {e}')
        raise Exception(f'Error while creating Ticker item {dto.model_dump()}')


    return db_obj

def find_all(db: Session) -> list[Ticker]:
    return db.query(Ticker).order_by(Ticker.ticker).all()

def find_one(db: Session, dto: TickerDTO) -> Ticker:
    return db.query(Ticker).where(Ticker.ticker == dto.ticker).first()



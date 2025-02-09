from sqlalchemy import Column, Integer, Date, Double, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from src.infra.database import Base
from src.models.ticker import Ticker


class Market(Base):
    __tablename__ = 'tb_market'

    id = Column(Integer, autoincrement=True, primary_key=True)

    Date = Column(Date, nullable=False)

    Close = Column(Double, nullable=False)
    High = Column(Double, nullable=False)
    Low = Column(Double, nullable=False)
    Open = Column(Double, nullable=False)
    Volume = Column(Double, nullable=False)

    ticker_id = mapped_column(Integer, ForeignKey('tb_tickers.id'), nullable=False)
    ticker: Mapped["Ticker"] = relationship()


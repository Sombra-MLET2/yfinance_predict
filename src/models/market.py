from sqlalchemy import Column, Integer, Date, Double, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from src.infra.database import Base
from src.models.ticker import Ticker


class Market(Base):
    __tablename__ = 'tb_market'

    id = Column(Integer, autoincrement=True, primary_key=True)

    date = Column(Date, nullable=False)

    close = Column(Double, nullable=False)
    high = Column(Double, nullable=False)
    low = Column(Double, nullable=False)
    open = Column(Double, nullable=False)
    volume = Column(Double, nullable=False)

    ticker_id = mapped_column(Integer, ForeignKey('tb_tickers.id'), nullable=False)
    ticker: Mapped["Ticker"] = relationship()


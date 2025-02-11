from sqlalchemy import Column, Integer, Date, Double, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped
from infra.database import Base
from models.stock import Stock


class Market(Base):
    __tablename__ = 'tb_market'

    id = Column(Integer, autoincrement=True, primary_key=True)

    date = Column(Date, nullable=False)

    close = Column(Double, nullable=False)
    high = Column(Double, nullable=False)
    low = Column(Double, nullable=False)
    open = Column(Double, nullable=False)
    volume = Column(Double, nullable=False)

    stock_id = mapped_column(Integer, ForeignKey('tb_stocks.id'), nullable=False)
    stock: Mapped["Stock"] = relationship()


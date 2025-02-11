from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from infra.database import Base


class Stock(Base):
    __tablename__ = 'tb_stocks'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ticker = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    businessSummary = Column(String, nullable=False)

    market = relationship('Market', backref = 'Stock')
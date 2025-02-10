from sqlalchemy import Column, Integer, String
from infra.database import Base


class Ticker(Base):
    __tablename__ = 'tb_tickers'

    id = Column(Integer, autoincrement=True, primary_key=True)
    ticker = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    sector = Column(String, nullable=False)
    businessSummary = Column(String, nullable=False)
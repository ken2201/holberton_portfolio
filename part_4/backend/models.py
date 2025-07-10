from sqlalchemy import Column, Integer, String, Float, Date
from backend.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    category = Column(String)
    amount = Column(Float)
    date = Column(Date)


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String, index=True)
    amount = Column(Float)

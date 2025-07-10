from pydantic import BaseModel
from datetime import date


class TransactionBase(BaseModel):
    type: str
    category: str
    amount: float
    date: date


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int

    class Config:
        from_attributes = True



class BudgetBase(BaseModel):
    month: str
    amount: float


class BudgetCreate(BudgetBase):
    pass


class Budget(BudgetBase):
    id: int

    class Config:
        from_attributes = True

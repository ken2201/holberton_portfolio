from sqlalchemy.orm import Session
from backend.models import Transaction, Budget
from backend.schemas import TransactionCreate, BudgetCreate


def create_transaction(db: Session, transaction: TransactionCreate):
    db_item = Transaction(**transaction.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_transactions(db: Session):
    return db.query(Transaction).all()


def delete_transaction(db: Session, transaction_id: int):
    db_item = db.query(Transaction).filter(
        Transaction.id == transaction_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item


def set_budget(db: Session, budget: BudgetCreate):
    existing = db.query(Budget).filter(Budget.month == budget.month).first()
    if existing:
        existing.amount = budget.amount
        db.commit()
        db.refresh(existing)
        return existing
    new_budget = Budget(**budget.dict())
    db.add(new_budget)
    db.commit()
    db.refresh(new_budget)
    return new_budget


def get_budget(db: Session, month: str):
    return db.query(Budget).filter(Budget.month == month).first()

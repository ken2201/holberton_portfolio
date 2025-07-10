from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.models import Transaction
from backend.database import SessionLocal
from sqlalchemy import func

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def get_summary(db: Session = Depends(get_db)):
    income = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == "income").scalar() or 0
    expenses = db.query(func.sum(Transaction.amount)).filter(
        Transaction.type == "expense").scalar() or 0
    balance = income - expenses
    return {
        "income": income,
        "expenses": expenses,
        "balance": balance
    }

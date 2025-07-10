# backend/routers/transactions.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import Transaction, TransactionCreate
from backend.crud import create_transaction, get_transactions, delete_transaction
from backend.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Transaction)
def add_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction)

@router.get("/", response_model=list[Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return get_transactions(db)

@router.delete("/{transaction_id}", response_model=Transaction)
def remove_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = delete_transaction(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

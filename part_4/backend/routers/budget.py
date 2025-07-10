from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas import Budget, BudgetCreate
from backend.crud import set_budget, get_budget
from backend.database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Budget)
def create_or_update_budget(budget: BudgetCreate, db: Session = Depends(get_db)):
    return set_budget(db, budget)


@router.get("/{month}", response_model=Budget)
def read_budget(month: str, db: Session = Depends(get_db)):
    budget = get_budget(db, month)
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return budget

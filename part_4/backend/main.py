from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.database import Base, engine
from backend.routers import transactions, budget, summary

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS setup for frontend on Vite (localhost:8080)
app.add_middleware(
    CORSMiddleware,
    # or use ["*"] for all origins during development
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(transactions.router,
                   prefix="/api/transactions", tags=["Transactions"])
app.include_router(budget.router, prefix="/api/budget", tags=["Budget"])
app.include_router(summary.router, prefix="/api/summary", tags=["Summary"])

import logging
from fastapi import FastAPI
import src.infra.configs as configs
from src.infra.database import engine, Base
from src.sessions.route import sessions_router
from src.market.route import market_router

logging.info(f"*** Yahoo finance predict - API running on {configs.ENV} environment ***")

app = FastAPI()

app.include_router(sessions_router)
app.include_router(market_router)

# SQLAlchemy create tables
Base.metadata.create_all(bind=engine)

@app.get("/",
         tags=["tech-challenge"],
         summary="Team & Project Info")
async def root():
    return {
        "FIAP": {
            "success": True,
            "tech_challenge": "Phase - Yahoo finance predict",
            "team": "Sombra-MLET2"
        }
    }

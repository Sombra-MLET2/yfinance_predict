import logging
from fastapi import FastAPI
import infra.configs as configs
from infra.database import engine, Base
from sessions.route import sessions_router
from routes.market_route import market_router
from routes.stock_route import stock_router
from src.routes.predict_route import predict_router

logging.info(f"*** Yahoo finance predict - API running on {configs.ENV} environment ***")

app = FastAPI()

app.include_router(sessions_router)
app.include_router(market_router)
app.include_router(stock_router)
app.include_router(predict_router)

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

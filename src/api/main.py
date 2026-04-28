from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.core.config import settings
from src.core.logger import logger
from src.api.routes import prediction

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application Startup")
    yield 

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0",
    lifespan=lifespan
)
    
@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message" : f"{settings.app_name} is running"}

app.include_router(prediction.router)
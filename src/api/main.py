from fastapi import FastAPI
from src.core.config import Settings, settings
from src.core.logger import logger

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0"
)
@app.on_event("startup")
def startup_event():
    logger.info("Application Startup")
    
@app.get("/")
def root():
    logger.info("Root endpoint called")
    return {"message" : f"{settings.app_name} is running"}
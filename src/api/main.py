from fastapi import FastAPI
from src.core.config import Settings, settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message" : f"{settings.app_name} is running"}
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    app_name: str = "Loan Eligibility Risk Scoring API"
    debug: bool = True
    model_path: str = str(BASE_DIR / "models" / "model.joblib")
    preprocessor_path: str = str(BASE_DIR / "models" / "preprocessor.joblib")
    model_config = SettingsConfigDict(env_file=".env")
    threshold: float = 0.20

settings = Settings()
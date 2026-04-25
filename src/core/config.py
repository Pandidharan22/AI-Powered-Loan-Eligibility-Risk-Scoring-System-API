from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Loan Eligibility Risk Scoring API"
    debug: bool = True
    model_path: str = "models/model.joblib"
    preprocessor_path = "models/preprocessor.joblib"
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
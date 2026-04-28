import pandas as pd
from src.services.model_service import model_service
from src.core.config import settings
from sklearn.ensemble import GradientBoostingClassifier
from src.pipeline.preprocessing import DataPreprocessor

class PredictionService:
    def __init__(self):
        self.model: GradientBoostingClassifier = model_service.get_model()
        self.preprocessor: DataPreprocessor = model_service.get_preprocessor()

    def predict(self, data: dict):
        df = pd.DataFrame([data])

        df["LoanID"] = "API_INPUT"

        X_transformed = self.preprocessor.transform(df)

        proba = self.model.predict_proba(X_transformed)[0][1]

        prediction = int(proba >= settings.threshold)

        return {
            "default_probability": float(proba),
            "prediction": prediction
        }


prediction_service = PredictionService()
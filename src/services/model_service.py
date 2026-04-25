import joblib
from src.core.config import settings


class ModelService:
    def __init__(self):
        self.model = None
        self.preprocessor = None

    def load_models(self):
        if self.model is None or self.preprocessor is None:
            self.model = joblib.load(settings.model_path)
            self.preprocessor = joblib.load(settings.preprocessor_path)

    def get_model(self):
        if self.model is None:
            self.load_models()
        return self.model

    def get_preprocessor(self):
        if self.preprocessor is None:
            self.load_models()
        return self.preprocessor


model_service = ModelService()
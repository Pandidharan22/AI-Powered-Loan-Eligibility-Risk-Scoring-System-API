import joblib
from sklearn.ensemble import GradientBoostingClassifier
from src.pipeline.preprocessing import DataPreprocessor
from src.core.config import settings


class ModelService:
    def __init__(self):
        self.model : GradientBoostingClassifier | None = None
        self.preprocessor : DataPreprocessor | None = None

    def load_models(self):
        if self.model is None or self.preprocessor is None:
            self.model = joblib.load(settings.model_path)
            self.preprocessor = joblib.load(settings.preprocessor_path)

    def get_model(self) -> GradientBoostingClassifier:
        if self.model is None:
            self.load_models()
        assert self.model is not None
        return self.model

    def get_preprocessor(self) -> DataPreprocessor:
        if self.preprocessor is None:
            self.load_models()
        assert self.preprocessor is not None
        return self.preprocessor


model_service = ModelService()
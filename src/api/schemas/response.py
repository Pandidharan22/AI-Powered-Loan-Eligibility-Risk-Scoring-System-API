from pydantic import BaseModel

class PredictionResponse(BaseModel):
    default_probability: float
    prediction: int
from fastapi import APIRouter, HTTPException
from src.api.schemas.request import PredictionRequest
from src.api.schemas.response import PredictionResponse
from src.services.prediction_service import prediction_service

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        result = prediction_service.predict(request.model_dump())
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
from fastapi import APIRouter, HTTPException
from src.api.schemas.request import PredictionRequest
from src.api.schemas.response import PredictionResponse
from src.services.prediction_service import prediction_service

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        return prediction_service.predict(request.model_dump())

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )
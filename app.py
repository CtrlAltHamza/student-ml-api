from fastapi import FastAPI
from pydantic import BaseModel


VERSION = "1.1.0"
APPLICATION = "student-ml-api"
MODEL_VERSION = "model-1"

app = FastAPI(title=APPLICATION, version=VERSION)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "healthy",
        "application": APPLICATION,
        "application_version": VERSION,
        "model_version": MODEL_VERSION,
    }


@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, float]:
    return {"input": request.value, "prediction": request.value * 2}
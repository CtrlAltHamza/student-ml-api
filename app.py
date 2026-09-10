from fastapi import FastAPI
from pydantic import BaseModel


VERSION = "1.0.0"
APPLICATION = "student-ml-api"

app = FastAPI(title=APPLICATION, version=VERSION)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy", "application": APPLICATION, "version": VERSION}


@app.post("/predict")
def predict(request: PredictionRequest) -> dict[str, float]:
    return {"input": request.value, "prediction": request.value * 2}
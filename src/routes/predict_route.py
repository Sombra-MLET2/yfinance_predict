import os
from typing import List
from venv import logger

import joblib
import numpy as np
import pandas as pd
from fastapi import APIRouter
from keras.src.saving import load_model
from tensorflow.python.keras import Sequential

from src.dtos.predict_dto import PredictRequest, PredictResponse

model = None
scaler = None

predict_router = APIRouter(
    prefix="/predictions",
    tags=["predictions"],
    responses={401: {"description": "Invalid credentials"},
               404: {"description": "Not found"},
               500: {"description": "Internal server error"}},
)


@predict_router.post("/", response_model=PredictResponse)
def predict(request: PredictRequest):
    logger.info("Recebida requisição para predicao:", request.dict())

    dfs = map_dto_to_df([request])
    pre_processed = pre_process(dfs)

    global model
    global scaler

    if model is None:
        model = load_keras_model()

    predict_amount = scale_prediction(model.predict(pre_processed))

    return PredictResponse(prediction=predict_amount[0])


def path_models(param):
    if os.environ.get("ENV") == "prod":
        return f"/opt/app/models/{param}"

    return f"predict_model/{param}"


def scale_prediction(predictions):
    global scaler

    if scaler is None:
        scaler = joblib.load(path_models("scaler.gz"))

    y_test_aux = np.zeros((1, 5))
    y_test_aux[:, -1] = predictions[0][0]
    return scaler.inverse_transform(y_test_aux)[:, -1]


def pre_process(data):
    global scaler
    if scaler is None:
        scaler = joblib.load(path_models("scaler.gz"))

    scaled = scaler.transform(data)
    single_row = scaled[:, :4]

    single_row = single_row.flatten()

    sequence = np.tile(single_row, (60, 1))
    batch = np.expand_dims(sequence, axis=0)

    return batch


def load_keras_model() -> Sequential:
    return load_model(path_models("model.keras"))


def map_dto_to_df(data: List[PredictRequest]) -> pd.DataFrame:

    data_dicts = []
    for dto in data:
        data_dict = dto.dict()
        data_dict['Close'] = 0.0

        data_dicts.append(data_dict)

    return pd.DataFrame(data_dicts)
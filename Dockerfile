FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    NEW_RELIC_APP_NAME="yFinance Predict" \
    PYTHONPATH=./src \
    ENV=prod

ARG NEW_RELIC_LICENSE_KEY=abc123
ENV NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY

WORKDIR /opt/app/

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

COPY src ./src
COPY /predict_model/model.keras ./models/model.keras
COPY /predict_model/scaler.gz ./models/scaler.gz

EXPOSE 80

CMD ["newrelic-admin", "run-program", \
        "uvicorn", "src.main:app",\
        "--host", "0.0.0.0",\
        "--port", "80"]
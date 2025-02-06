FROM python:3.12-slim
ARG NEW_RELIC_LICENSE_KEY=abc123

MAINTAINER SombraTeam - https://github.com/Sombra-MLET2

ENV NEW_RELIC_APP_NAME="yFinance Predict"
ENV NEW_RELIC_LICENSE_KEY=$NEW_RELIC_LICENSE_KEY

WORKDIR /opt/

COPY /src ./app/src
COPY requirements.txt ./app/

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./app/requirements.txt

WORKDIR /opt/app/

EXPOSE 80

CMD ["newrelic-admin", "run-program", \
        "uvicorn", "src.main:app",\
        "--host", "0.0.0.0",\
        "--port", "80"]
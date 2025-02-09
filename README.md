# Configuration

## Requirement

Python version 3.10.16

## Setup Virtual Environment

1. Create a Virtual Environment
```bash
    python -m venv venv
```

2. Active the Virtual Environment
```bash
    source .venv/bin/activate
```

3. Install Dependencies
```bash
    pip install -r requirements.txt
```

4. Running the API
```bash
    fastapi run src/main.py
```

5. Building & Running the Docker image
    1. Acquire an API Key

```bash
    docker build --build-arg NEW_RELIC_LICENSE_KEY=<API_KEY> -t sombra/yfinance .
    docker run --rm -p 8080:80 sombra/yfinance
```
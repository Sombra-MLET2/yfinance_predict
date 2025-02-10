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

# Model Score

<!-- START_SCORE -->
```
Mean Absolute Error(MAE): 3.0468259825977526
Mean Absolute Percentage Error(MAPE): 0.06285272196782521%
Root Mean Squared Error(RMSE): 4.072522089201633
Mean Squared Error(MSE): 16.58543616703523
R2: 0.9917744158898466
EV: 0.9960871326953288
```
<!-- END_SCORE -->

![scatter](./predict_model/metrics/real_vs_predicted.png)

![scatter](./predict_model/metrics/scatter.png)
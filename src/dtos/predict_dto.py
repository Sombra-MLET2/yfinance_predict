from pydantic import BaseModel


# Prediction Request
class PredictRequest(BaseModel):
    Open: float
    High: float
    Low: float
    Volume: float

    def get_array(self):
        return [self.open, self.high, self.low, self.volume]

# Prediction REsponse
class PredictResponse(BaseModel):
    prediction: float
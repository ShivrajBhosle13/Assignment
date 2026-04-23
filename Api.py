from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/v1/market-data")
def get_data():
    if random.random() < 0.05:
        return {"error": "Random failure"}
    return [{
        "instrument_id": "AAPL",
        "price": 180.25,
        "volume": 1000,
        "timestamp": "2026-04-20T10:00:00Z"
    }]

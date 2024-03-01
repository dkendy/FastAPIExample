from fastapi import FastAPI
from trainmodel import train_and_evaluate_model

app = FastAPI()

@app.post("/train_and_evaluate")
async def train_and_evaluate(test_size: float = 0.2, random_state: int = 42, n_neighbors: int = 3):
    accuracy = train_and_evaluate_model(test_size, random_state, n_neighbors)
    return {"accuracy": accuracy}


@app.get("/")
async def train_and_evaluate():
    accuracy = train_and_evaluate_model(0.2, 42, 3)
    return {"get_accuracy": accuracy}

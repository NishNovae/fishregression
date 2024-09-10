from fastapi import FastAPI
import pickle
from fishregression.regressor import grab_path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Wordl!", "This is": "fishregression"}

def run_prediction(length: float):
    model_path = grab_path("model.pkl")
    with open(model_path, "rb") as model:
        lr = pickle.load(model)
    pred = lr.predict([[length**2, length]])     # polynomial regression
    return float(r[0])


@app.get("/fish")
def fish(length: float):
    weight = run_prediction(length)
    return { "length": length, "weight": weight }

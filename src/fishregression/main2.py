from fastapi import FastAPI
import pickle
from fishregression.pathfinder import grab_path

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World!", "This is": "fishclassification"}

def run_prediction(length: float, weight: float):
    model_path = grab_path("classifier.pkl")
    with open(model_path, "rb") as model:
        kn = pickle.load(model)
    pred = kn.predict([[length, weight]])
    answer = "Smelt" if pred[0] == 1 else "Bream"
    return answer

@app.get("/fish")
def fish(length: float, weight: float):
    answer = run_prediction(length, weight)
    return { "length": length, "weight": weight, "answer": answer }

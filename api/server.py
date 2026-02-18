from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Allow your frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data", "output")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail=f"{filename} not found")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/")
def home():
    return {
        "status": "API is running",
        "categories": ["watches", "jewelry", "footwear"]
    }

@app.get("/products/watches")
def get_watches():
    return load_json("watch_products.json")

@app.get("/products/jewelry")
def get_jewelry():
    return load_json("jewelry_products.json")

@app.get("/products/footwear")
def get_footwear():
    return load_json("footwear_products.json")

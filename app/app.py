"""Module defining the app."""
from fastapi import FastAPI
from typing import List

from app.contract_optimizer import find_optimal_path
from app.models import Contract, OptimalPath

app = FastAPI()


@app.post("/spaceship/optimize",
          response_model=OptimalPath)
def spaceship_optimizer(contracts: List[Contract]):
    contracts = [c.dict() for c in contracts]
    income, path = find_optimal_path(contracts)
    return {"income": income, "path": path}

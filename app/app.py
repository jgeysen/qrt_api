"""Module defining the app."""
from typing import List

from fastapi import FastAPI

from app.contract_optimizer import find_optimal_path_and_income
from app.models import Contract, OptimalPath

app = FastAPI()


@app.post("/spaceship/optimize", response_model=OptimalPath)
def spaceship_optimizer(contracts: List[Contract]) -> dict[str]:
    """Returns the optimal combination of contracts which result in the
    highest income.

    Args:
        contracts: a list of contracts according to the pydantic Contract model.

    Returns:
        dict[str]: dictionary containing the maximal obtainable income and the
        path of contract names to realise that income.
    """
    contracts = [c.dict() for c in contracts]
    income, path = find_optimal_path_and_income(contracts)
    return {"income": income, "path": path}

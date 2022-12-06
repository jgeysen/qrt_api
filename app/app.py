"""Module defining the app."""
from typing import List

from fastapi import FastAPI

from app.contract_optimizer import ContractOptimiser
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
    contract_optimiser = ContractOptimiser(contracts=contracts)
    income, path = contract_optimiser.find_optimum()
    return {"income": income, "path": path}

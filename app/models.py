"""Modules for validation of input and output data."""
from typing import List

from pydantic import BaseModel


class Contract(BaseModel):
    """
    Class to represent a contract.
    """

    name: str
    start: int
    price: int
    duration: int


class OptimalPath(BaseModel):
    """
    Class to represent a dictionary containing an optimal path and income.
    """

    income: int
    path: List[str]

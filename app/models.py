"""Modules for validation of input and output data."""
from typing import List

from pydantic import BaseModel


class Contract(BaseModel):
    """ """

    name: str
    start: int
    price: int
    duration: int


class OptimalPath(BaseModel):
    """ """

    income: int
    path: List[str]

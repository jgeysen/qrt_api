"""Modules for validation of input and output data."""
from pydantic import BaseModel
from typing import List


class Contract(BaseModel):
	"""
	"""
	name: str
	start: int
	price: int
	duration: int


class OptimalPath(BaseModel):
	"""
	"""
	income: int
	path: List[str]

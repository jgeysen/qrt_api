"""Module testing the models in app/models.py."""
from app.models import Contract, OptimalPath


def test_contract():
    """
    Given input information for a Contract model,
    When the Contract model is initialised,
    Then the expected attributes are initialised.
    """
    name = "Contract1"
    start = 1
    price = 2
    duration = 2
    contract = Contract(name=name, start=start, price=price, duration=duration)

    assert contract.name == name
    assert contract.start == start
    assert contract.price == price
    assert contract.duration == duration


def test_optimal_path():
    """
    Given input information for a OptimalPath model,
    When the OptimalPath model is initialised,
    Then the expected attributes are initialised.
    """
    income = 10
    path = ["Contract1", "Contract2"]
    optimal_path = OptimalPath(income=income, path=path)

    assert optimal_path.income == income
    assert optimal_path.path == path

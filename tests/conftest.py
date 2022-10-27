"""Module defining fixtures used in testing the app."""
import pytest

from app.models import Contract


@pytest.fixture(scope="module")
def unsorted_contracts_fixture():
    """
    Fixture returning the list of contracts as given in the assignment.

    Returns:
        List[dict]: A list of contracts.
    """
    contracts = [
        {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "duration": 9, "price": 7},
    ]
    return contracts


@pytest.fixture(scope="module")
def sorted_contracts_fixture():
    """
    Fixture returning the list of contracts as given in the assignment. Also,
    the `end` key is added to each contract, indicating when the contract ends.

    Returns:
        List[dict]: A list of contracts.
    """
    contracts = [
        {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "end": 10, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "end": 14, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    return contracts


@pytest.fixture(scope="module")
def contracts_multiple_at_start_fixture():
    """
    Fixture returning a list of contracts where multiple contracts start
    at hour 0.

    Returns:
        List[dict]: A list of contracts.
    """
    contracts = [
        {"name": "Contract1", "start": 0, "end": 1, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 0, "end": 2, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 0, "end": 3, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    return contracts


@pytest.fixture(scope="module")
def contracts_overlapping_fixture():
    """
    Fixture returning a list of contracts which are only overlapping in time,
    but with different hourly prices.

    Returns:
        List[dict]: A list of contracts.
    """
    contracts = [
        {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 0, "end": 5, "duration": 5, "price": 11},
        {"name": "Contract3", "start": 0, "end": 5, "duration": 5, "price": 12},
    ]
    return contracts


@pytest.fixture(scope="module")
def unsorted_contract_models_fixture(unsorted_contracts_fixture):
    """
    Fixture returning a list of contract models. This is the input of the
    `spaceship_optimizer` method in the `app/app.py` module.

    Args:
        List[dict]: The unsorted contracts fixture is used here to create the
        contract models.
    Returns:
        List[Contract]: A list of contract models.
    """
    contract_models = []
    for contract in unsorted_contracts_fixture:
        contract_models.append(Contract.parse_obj(contract))

    return contract_models

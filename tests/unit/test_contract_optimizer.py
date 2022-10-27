"""Module testing the contract_optimizer module."""
from unittest.mock import patch

from app.contract_optimizer import (
    find_optimal_path_and_income,
    find_optimum,
    get_eligible_contracts,
)


@patch("app.contract_optimizer.find_optimum")
def test_find_optimal_path_and_income(
    mock_find_optimum,
    unsorted_contracts_fixture,
):
    """
    Given an unsorted list of contracts and mocked `find_optimum` method,
    When the `find_optimal_path_and_income` method is called on the unsorted list of
    contracts,
    Then the mocked `find_optimum` method is called with start hour 0 and index 0
    and the mocked return values are passed on to `find_optimal_path_and_income`.
    """
    mock_find_optimum.return_value = (10, ["Contract1", "Contract2"])
    income, path = find_optimal_path_and_income(unsorted_contracts_fixture)
    assert income == 10
    assert path == ["Contract1", "Contract2"]
    assert mock_find_optimum.called_once_with(0, 0)


def test_find_optimum_example(sorted_contracts_fixture):
    """
    Given a sorted list of contracts,
    When the `find_optimum` method is called starting from hour 0 and index 0,
    Then the expected optimal path and price are returned.
    """
    with patch("app.contract_optimizer.contracts", sorted_contracts_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 18
        assert path == ["Contract1", "Contract3"]


def test_find_optimum_single_contract():
    """
    Given a list of a single contract,
    When the `find_optimum` method is called starting from hour 0 and index 0,
    Then the optimal path just consists of the single contract and its price.
    """
    contracts = [
        {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
    ]

    with patch("app.contract_optimizer.contracts", contracts):
        total_price, path = find_optimum(0, 0)
        assert total_price == 10
        assert path == ["Contract1"]


def test_find_optimum_no_contract():
    """
    Given an empty list,
    When the `find_optimum` method is called starting from hour 0 and index 0,
    Then the optimal path is also empty.
    """
    contracts = []

    with patch("app.contract_optimizer.contracts", contracts):
        total_price, path = find_optimum(0, 0)
        assert total_price == 0
        assert path == []


def test_find_optimum_multiple_at_start(contracts_multiple_at_start_fixture):
    """
    Given a list of contracts where most of the contracts start at hour 0,
    When the `find_optimum` method is called starting from hour 0 and index 0,
    Then the expected optimal path and price are returned; the most lucrative contract
    starting at hour 0 combined with the only other possible contract.
    """
    with patch("app.contract_optimizer.contracts", contracts_multiple_at_start_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 21
        assert path == ["Contract2", "Contract4"]


def test_find_optimum_only_overlapping(contracts_overlapping_fixture):
    """
    Given a list of overlapping contracts,
    When the `find_optimum` method is called starting from hour 0 and index 0,
    Then the expected optimal path and price are returned; as all contracts overlap,
    this would be a single contract with the highest price.
    """
    with patch("app.contract_optimizer.contracts", contracts_overlapping_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 12
        assert path == ["Contract3"]


def test_get_eligible_contracts_example_start_0(sorted_contracts_fixture):
    """
    Given a list of sorted contracts,
    When the `get_eligible_contracts` method is called where the eligible contracts can
    start anywhere after or on hour 0,
    Then all contracts are returned.
    """
    with patch("app.contract_optimizer.contracts", sorted_contracts_fixture):
        contracts = get_eligible_contracts(0, 0)
        assert contracts == sorted_contracts_fixture


def test_get_eligible_contracts_example_start_5(sorted_contracts_fixture):
    """
    Given a list of sorted contracts,
    When `get_eligible_contracts` method is called where the eligible contracts
    should start on or after hour 5,
    Then only the contracts which start after or on hour 5 are returned.
    """
    result = [
        {"name": "Contract3", "start": 5, "end": 14, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    with patch("app.contract_optimizer.contracts", sorted_contracts_fixture):
        contracts = get_eligible_contracts(0, 5)
        assert contracts == result


def test_get_eligible_contracts_multiple_start_3(contracts_multiple_at_start_fixture):
    """
    Given a list of contracts where multiple contracts start at hour 0,
    When `get_eligible_contracts` method is called where the eligible contracts
    should start on or after hour 3,
    Then only the contracts which start after or on hour 3 are returned.
    """
    result = [
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    with patch("app.contract_optimizer.contracts", contracts_multiple_at_start_fixture):
        contracts = get_eligible_contracts(0, 3)
        assert contracts == result

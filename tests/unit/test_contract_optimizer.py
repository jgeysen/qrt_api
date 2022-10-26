"""Module testing the contract_optimizer module."""
from unittest.mock import patch

from app.contract_optimizer import (find_optimal_path_and_income, find_optimum,
                                    get_eligible_contracts)


@patch("app.contract_optimizer.find_optimum")
def test_find_optimal_path_and_income(
    mock_find_optimum,
    unsorted_contracts_fixture,
):
    mock_find_optimum.return_value = (10, ["Contract1", "Contract2"])
    income, path = find_optimal_path_and_income(unsorted_contracts_fixture)
    assert income == 10
    assert path == ["Contract1", "Contract2"]
    assert mock_find_optimum.called_once_with(0, 0)


def test_find_optimum_example(contracts_example_fixture):
    with patch("app.contract_optimizer.contracts", contracts_example_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 18
        assert path == ["Contract1", "Contract3"]


def test_find_optimum_single_contract():
    contracts = [
        {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
    ]

    with patch("app.contract_optimizer.contracts", contracts):
        total_price, path = find_optimum(0, 0)
        assert total_price == 10
        assert path == ["Contract1"]


def test_find_optimum_multiple_at_start(contracts_multiple_at_start_fixture):
    with patch("app.contract_optimizer.contracts", contracts_multiple_at_start_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 21
        assert path == ["Contract2", "Contract4"]


def test_find_optimum_only_overlapping(contracts_overlapping_fixture):

    with patch("app.contract_optimizer.contracts", contracts_overlapping_fixture):
        total_price, path = find_optimum(0, 0)
        assert total_price == 12
        assert path == ["Contract3"]


def test_get_eligible_contracts_example_start_0(contracts_example_fixture):
    with patch("app.contract_optimizer.contracts", contracts_example_fixture):
        contracts = get_eligible_contracts(0, 0)
        assert contracts == contracts_example_fixture


def test_get_eligible_contracts_example_start_5(contracts_example_fixture):
    result = [
        {"name": "Contract3", "start": 5, "end": 14, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    with patch("app.contract_optimizer.contracts", contracts_example_fixture):
        contracts = get_eligible_contracts(0, 5)
        assert contracts == result


def test_get_eligible_contracts_multiple_start_3(contracts_multiple_at_start_fixture):
    result = [
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]
    with patch("app.contract_optimizer.contracts", contracts_multiple_at_start_fixture):
        contracts = get_eligible_contracts(0, 3)
        assert contracts == result

"""Module testing the methods defined in app/app.py."""
from unittest.mock import patch

from app.app import spaceship_optimizer


@patch("app.app.find_optimal_path_and_income")
def test_spaceship_optimizer(
    mock_find_optimal_path_and_income,
    unsorted_contract_models_fixture,
    unsorted_contracts_fixture,
):
    """
    Given a list of contract models, a list of unsorted contracts and
    a mocked instance of the find_optimal_path_and_income method,
    When the `spaceship_optimizer` is invoked with a list of contract
    models,
    Then the mocked method is called with the unsorted contracts and the
    mocked return values are asserted.
    """
    mock_find_optimal_path_and_income.return_value = (10, ["Contract1", "Contract2"])
    result = spaceship_optimizer(unsorted_contract_models_fixture)

    assert mock_find_optimal_path_and_income.called_once_with(
        unsorted_contracts_fixture
    )
    assert result.get("income") == 10
    assert result.get("path") == ["Contract1", "Contract2"]

"""Module testing the contract_optimizer module."""
import sys
import time

import pytest

from app.contract_optimizer import ContractOptimiser


class TestContractOptimiser:
    def test_find_optimum_example(self, sorted_contracts_fixture):
        """
        Given a sorted list of contracts,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the expected optimal path and price are returned.
        """
        contract_optimiser = ContractOptimiser(contracts=sorted_contracts_fixture)
        total_price, path = contract_optimiser.find_optimum()
        assert total_price == 18
        assert path == ["Contract1", "Contract3"]

    def test_find_optimum_single_contract(self):
        """
        Given a list of a single contract,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the optimal path just consists of the single contract and its price.
        """
        contracts = [
            {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
        ]

        contract_optimiser = ContractOptimiser(contracts=contracts)
        total_price, path = contract_optimiser.find_optimum()
        assert total_price == 10
        assert path == ["Contract1"]

    def test_find_optimum_no_contract(self):
        """
        Given an empty list,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the optimal path is also empty.
        """
        contracts = []

        contract_optimiser = ContractOptimiser(contracts=contracts)
        total_price, path = contract_optimiser.find_optimum()
        assert total_price == 0
        assert path == []

    def test_find_optimum_multiple_at_start(self, contracts_multiple_at_start_fixture):
        """
        Given a list of contracts where most of the contracts start at hour 0,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the expected optimal path and price are returned; the most lucrative contract
        starting at hour 0 combined with the only other possible contract.
        """
        contract_optimiser = ContractOptimiser(
            contracts=contracts_multiple_at_start_fixture
        )
        total_price, path = contract_optimiser.find_optimum()
        assert total_price == 21
        assert path == ["Contract2", "Contract4"]

    def test_find_optimum_only_overlapping(self, contracts_overlapping_fixture):
        """
        Given a list of overlapping contracts,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the expected optimal path and price are returned; as all contracts overlap,
        this would be a single contract with the highest price.
        """
        contract_optimiser = ContractOptimiser(contracts=contracts_overlapping_fixture)
        total_price, path = contract_optimiser.find_optimum()
        assert total_price == 12
        assert path == ["Contract3"]

    @pytest.mark.performance
    def test_find_optimum_5k_contracts(self, sorted_contracts_1k_fixture):
        """
        Given a list of 5000 contracts,
        When the `find_optimum` method is called starting from hour 0 and index 0,
        Then the method finishes successfully under 10 seconds.
        """
        contract_optimiser = ContractOptimiser(contracts=sorted_contracts_1k_fixture)
        sys.setrecursionlimit(len(sorted_contracts_1k_fixture) * 2)
        tic = time.perf_counter()
        contract_optimiser.find_optimum()
        toc = time.perf_counter()
        assert toc - tic < 10

    def test_get_next_eligible_contract_id_example_start_0(
        self, sorted_contracts_fixture
    ):
        """
        Given a list of sorted contracts,
        When the `get_eligible_contracts` method is called where the eligible
        contracts can start anywhere after or on hour 0,
        Then all contracts are returned.
        """
        contract_optimiser = ContractOptimiser(contracts=sorted_contracts_fixture)
        contract_id = contract_optimiser._get_next_eligible_contract_id(0, 0)
        assert contract_id == 0

    def test_get_next_eligible_contract_id_example_start_5(
        self, sorted_contracts_fixture
    ):
        """
        Given a list of sorted contracts,
        When `get_eligible_contracts` method is called where the eligible contracts
        should start on or after hour 5,
        Then only the contracts which start after or on hour 5 are returned.
        """
        contract_optimiser = ContractOptimiser(contracts=sorted_contracts_fixture)
        contract_id = contract_optimiser._get_next_eligible_contract_id(5, 0)
        assert contract_id == 2

    def test_get_next_eligible_contract_id_multiple_start_3(
        self,
        contracts_multiple_at_start_fixture,
    ):
        """
        Given a list of contracts where multiple contracts start at hour 0,
        When `get_eligible_contracts` method is called where the eligible contracts
        should start on or after hour 3,
        Then only the contracts which start after or on hour 3 are returned.
        """
        contract_optimiser = ContractOptimiser(
            contracts=contracts_multiple_at_start_fixture
        )
        contract_id = contract_optimiser._get_next_eligible_contract_id(3, 0)
        assert contract_id == 3

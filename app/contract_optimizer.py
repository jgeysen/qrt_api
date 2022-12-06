"""Module defining the methods to find the optimal path of contracts."""
from typing import List


class ContractOptimiser:
    def __init__(self, contracts):
        self.contracts = contracts
        self.sorted_contracts = sorted(contracts, key=lambda d: d["start"])
        self._solution_cache = {}

    def find_optimum(self, start: int = 0, index: int = 0) -> tuple[int, List[str]]:
        """Finds the optimal combination of contracts in the global variable
        `contracts`.

        Starting from the timestamp `start` and index `index`, this method will
        calculate all feasible combinations of contracts and their total contract
        price in a recursive manner and will return the total price and path
        of the most price-optimal combination. The contracts in the global
        variable `contracts` are assumed to be sorted in ascending order
        according to the `start` attribute.

        Args:
            start: integer indicating an hour, beyond which the optimal search
            will start.
            index: index of the list of contracts. All contracts beyond this
            index will be searched.

        Returns:
            int: The total price of the most optimal contract combination.
            List[str]: List of contract names, which make up the  optimal
            combination of contracts.
        """
        income, path = self._solution_cache.get(start, (0, []))
        if income and path:
            return income, path

        first_contract_id = self._get_next_eligible_contract_id(start, index)
        second_contract_id = self._get_next_eligible_contract_id(start, index + 1)

        if first_contract_id == len(self.contracts):
            return 0, []

        first_contract = self.sorted_contracts[first_contract_id]
        first_contract["end"] = first_contract["start"] + first_contract["duration"]

        if second_contract_id == len(self.contracts):
            return first_contract.get("price"), [first_contract.get("name")]

        second_contract = self.sorted_contracts[second_contract_id]
        income, path = self._solution_cache.get(first_contract.get("end"), (0, []))

        if income and second_contract.get("start") >= first_contract.get("end"):
            return (
                first_contract.get("price") + income,
                [first_contract.get("name")] + path,
            )
        else:
            income_1, path_1 = self.find_optimum(first_contract.get("end"), index + 1)

        income_2, path_2 = self.find_optimum(start, index + 1)

        income_1 = first_contract.get("price") + income_1
        if income_1 >= income_2:
            path = [first_contract.get("name")] + path_1
            self._solution_cache.update({start: (income_1, path)})
            return income_1, path
        else:
            self._solution_cache.update({start: (income_2, path_2)})
            return income_2, path_2

    def _get_next_eligible_contract_id(self, start: int = 0, index: int = 0) -> int:
        """Finds the next contract in the global variable list of contracts.

        The next contract starts at the given `start` hour or right after.

        Args:
            start: All contracts in `contracts` which start on or after `start`
            will be returned.
            index: Only contracts after the id `index` are scanned, for efficiency.

        Returns:
            int: index of the next contract which starts on or after the `start`
            argument. The returned index is capped at the length of the global `contracts`
            variable.
        """
        while index < len(self.sorted_contracts):
            if self.sorted_contracts[index].get("start") >= start:
                return index
            index += 1

        return len(self.sorted_contracts)

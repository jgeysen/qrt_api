"""Module defining the methods to find the optimal path of contracts."""


def find_optimal_path(contracts):
    for x in contracts:
        x["end"] = x["start"] + x["duration"]
    sorted_contracts = sorted(contracts, key=lambda d: d["start"])
    income, path = find_max(0, 15, sorted_contracts)
    return income, path


def find_max(start, stop, contracts):
    """
    :param start:
    :param stop:
    :param contracts:
    :return:
    """
    eligible_contracts = [
        contract
        for contract in contracts
        if contract.get("start") >= start and contract.get("end") <= stop
    ]
    if not eligible_contracts:
        return 0, []
    first_contract = eligible_contracts[0]

    option_1 = find_max(first_contract.get("end"), stop, eligible_contracts[1:])
    option_2 = find_max(start, stop, eligible_contracts[1:])

    total_price_1 = first_contract.get("price") + option_1[0]
    total_price_2 = option_2[0]

    path_1 = option_1[1]
    path_2 = option_2[1]

    if total_price_1 >= total_price_2:
        path = [first_contract.get("name")] + path_1
        total_price = total_price_1

    else:
        path = path_2
        total_price = total_price_2

    return total_price, path

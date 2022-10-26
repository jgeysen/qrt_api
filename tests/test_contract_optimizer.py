from app.contract_optimizer import find_max


def test_find_max():
    contracts = [
        {"name": "Contract1", "start": 0, "end": 5, "duration": 5, "price": 10},
        {"name": "Contract2", "start": 3, "end": 10, "duration": 7, "price": 14},
        {"name": "Contract3", "start": 5, "end": 14, "duration": 9, "price": 8},
        {"name": "Contract4", "start": 6, "end": 15, "duration": 9, "price": 7},
    ]

    total_price, path = find_max(0, 15, contracts)
    assert total_price == 18
    assert path == ["Contract1", "Contract3"]

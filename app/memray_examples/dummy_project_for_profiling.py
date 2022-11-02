from app.contract_optimizer import find_optimal_path_and_income


contracts = [
	{"name": "Contract1", "start": 0, "duration": 5, "price": 10},
	{"name": "Contract2", "start": 3, "duration": 7, "price": 14},
	{"name": "Contract3", "start": 5, "duration": 9, "price": 8},
	{"name": "Contract4", "start": 6, "duration": 9, "price": 7},
]

find_optimal_path_and_income(contracts*100)

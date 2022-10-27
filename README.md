# Spaceship Rental Optimization API

A spaceship rental service with only a single spaceship for hire is facing a business 
problem: multiple bookings are requested, some of which are overlapping and at different
hourly rental prices. To find out what the optimal rental schedule looks like, the 
Spaceship Rental Optimization API was build. 

The Spaceship Rental Optimization API has only a single endpoint which is able 
to calculate the optimal rental period given a list of potential rental contracts.

## Structure

All the api logic sits in the `app` directory, in following files: 

- `app.py` contains the initialisation of the API and definition of the spaceship 
optimisation endpoint. 
- `contract_optimizer.py` contains the code which calculates the optimal rental window
and its total income.
- `models.py` contains pydantic models which help the spaceship optimisation endpoint
to validate its inputs and outputs.

## Run the App

There are two ways provided to run the application; in a docker container or in a 
virtual environment.

### With Docker

To run the app with docker, one needs to have the Docker Daemon running. If this is
the case, one can simply run `make server` from within the `qrt_api` directory. This 
command will build a docker image with -only- the strictly necessary packages installed
to run the app and spin up a container which exposes the endpoint on port `8080`.

### With a virtual environment

To run the app from within a virtual environment, one needs to have the dependency
manager `poetry` installed and a version of python `3.10`. 

If these requirements are met, one can install the app by following the next steps:

- Call `poetry install --no-dev` from the `qrt_api` directory, which will create a 
virtual environment.
- Activate the virtual environment by running `source .venv/bin/activate`.
- Start the app on port `8080` by running: `uvicorn app.app:app --host 0.0.0.0 --port 8080`

## Interact with the endpoint:

The app only has a single endpoint and the following scripts shows how one can easily
interact with the app. 

```python
import requests

contracts = [
    {"name": "Contract1", "start": 0, "duration": 5, "price": 10},
    {"name": "Contract2", "start": 3, "duration": 7, "price": 14},
    {"name": "Contract3", "start": 5, "duration": 9, "price": 8},
    {"name": "Contract4", "start": 6, "duration": 9, "price": 7},
]
url = "http://localhost:8080/spaceship/optimize/"

response = requests.post(url, json=contracts)

print(response.json())

```

## Check out the API documentation

After starting up the application, one can consult the swagger API documentation 
on `http://localhost:8080/docs`.

## Run the tests

Similar to running the app, one can run the tests within a docker container or within
a virtual environment: 

### With Docker

To run the app with docker, one needs to have the Docker Daemon running. If this is
the case, one can simply run `make test` from within the `qrt_api` directory. This 
command will build a docker image with the development packages installed
to run the tests and spin up a container which executes the `pytest` command. 

### With a virtual environment

To run the tests from within a virtual environment, one needs to have the dependency
manager `poetry` installed and a version of python `3.10`. 

If these requirements are met, one can run the tests by following the next steps:

- Call `poetry install` from the `qrt_api` directory, which will create a 
virtual environment with the dev packages installed. 
- Activate the virtual environment by running `source .venv/bin/activate`.
- Run `pytest`.

## Roadmap

Given more time and resources, following improvements could be made to the API:

- To make the search for the most optimal solution more efficient, one could
add a heuristic to the paths. A possible heuristic could be: the sum X of the prices 
of the remaining contracts. At any point during the search, when for branch A the 
current income + this sum X is lower than the current income of another branch B of 
the search, one could abandon branch A. A heuristic does require more overhead during 
the search. Worst case scenario, all the branches are still calculated with the 
overhead of calculating the heuristic. 
- In docker, the app is running as root. This is a potential security risk and should 
be addressed. 

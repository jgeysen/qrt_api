# Spaceship Rental Optimization API

A spaceship rental service with only a single spaceship for hire is facing a business 
problem: multiple bookings are requested, some of which are overlapping and some of 
which are at different hourly price points. To find out what the optimal rental 
schedule looks like, the Spaceship Rental Optimization API was build. 

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
command will: 
- Build a docker image with only the necessary packages installed
to run the app. 
- Spin up a container which exposes the endpoint on port `8080`.

To stop the server, run `make down`.

### With a virtual environment

To run the app from within a virtual environment, one needs to have the dependency
manager `poetry` installed and a version of python `3.10` (for example with `pyenv`). 

If these requirements are met, one can install the app by following the next steps:

- Run `poetry install --no-dev` from the `qrt_api` directory, which will create a 
virtual environment.
- Activate the virtual environment by running `source .venv/bin/activate`.
- Start the app on port `8080` by running: `uvicorn app.app:app --host 0.0.0.0 --port 8080`

## Interact with the endpoint:

The app has only a single endpoint and the following scripts shows how one can easily
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

To run the tests with docker, one needs to have the Docker Daemon running. If this is
the case, one can simply run `make test` from within the `qrt_api` directory. This 
command will: 

- Build a docker image with the development packages installed
to run the tests. 
- Spin up a container which executes the `pytest` command. 
- Optionally, if one wishes to run the perfomance tests, run `pytest -m performance`.

### With a virtual environment

To run the tests from within a virtual environment, one needs to have the dependency
manager `poetry` installed and a version of python `3.10` (for example with `pyenv`). 

If these requirements are met, one can run the tests by following the next steps:

- Call `poetry install` from the `qrt_api` directory, which will create a 
virtual environment with the dev packages installed. 
- Activate the virtual environment by running `source .venv/bin/activate`.
- Run `pytest`.
- Optionally, if one wishes to run the perfomance tests, run `pytest -m performance`.

## Roadmap

Given more time and resources, following improvements could be made to the API:

- When running the app in docker, the container is running as root. This is a 
security risk and should be addressed. 
- Write end2end tests. These tests would spin up the server and talk to the endpoint 
and follow a very similar pattern as the `Interact with the endpoint` example earlier 
in this `README.md`.
- Write an `OptimalPath` class within the `app/contract_optimizer.py` module. This
could avoid the use of the global variable `contracts`. 

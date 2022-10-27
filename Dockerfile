FROM python:3.10.0-slim as python-base

RUN pip install poetry
RUN poetry config virtualenvs.create false && \
    poetry config virtualenvs.in-project false

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock


FROM python-base as production-image
RUN poetry install --no-dev

FROM python-base as dev-image
RUN poetry install
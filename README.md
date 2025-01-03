# Habit tracker

Small Django backend to track habits. Based on:

- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/).
  > ⚠️ Note ⚠️
  >
  > As recommended in [the documentation](#https://docs.graphene-python.org/projects/django/en/latest/installation/#id1),
  > Graphene-Django is pinned to a specific version (3.2.2).

The data-schema is constituted of 3 tables: `User`, `Habit`, `Entry`.
Each row of `Entry` is linked to an `Habit`, which is linked to a `User`. 

The server is configured to connect to a PostgresDb instance.

A Rest API is provided for basic CRUD operations, while a GraphQL API is
available to retrieve aggregated data.

- Is GraphQL overkill for this project? Yes.
- Do I care? No.
- How about getting rid of the Rest API then? Meh.

## Setup

This project uses Python 3.13, and manages dependencies via `pyproject.toml`.

To install `poetry` as a packet manager, please refer to the
[official docs](https://python-poetry.org/docs/#installation).

## Getting Started

```bash
poetry install
```

## Virtual environment

Activate the virtual environment with:
```bash
poetry shell
```

Alternatively, you can prefix any command with `poetry run`. For instance:
```bash
poetry run python manage.py runserver
```

You can deactivate the virtual environment with:
```bash
exit
```

Or remove the virtual environment entirely (if needed):
```bash
# Commented for safety
# poetry env remove python
```

> NOTE
>
> In the following, `poetry run` is added as prefix to every command.
> It is nevertheless recommended to activate the virtual environment to avoid
> unintentional pollution of the system python installation.

### Export dependencies

You can export the dependency list into a `requirements.txt` file with:
```bash
# Generate `requirements.txt` form poetry
poetry export -f requirements.txt --output requirements.txt
```
or
```bash
pip freeze > requirements.txt
```

## OpenAPI Schema

OpenAPI v3 schema is available at `schemas/core.openapi.yml`.

## Development & housekeeping

A local docker image of Postgres can be run with:
```bash
docker compose up -d
```

after which, you can start the local development server with:
```bash
poetry run python manage.py runserver
```

Run the following command to tear down the Postgres instance:
```bash
docker compose down
```

### Code formatting / linting

You can format code by running:
```bash
poetry run black .
```

and check for linting errors with:
```bash
poetry run flake8 .
```

### Schema

[drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/readme.html)
is used to generate the API Schema. Upon updating the API, please make sure to
[annotate views](https://drf-spectacular.readthedocs.io/en/latest/readme.html#usage)
if needed, and regenerate the schema by running:

```bash
python manage.py spectacular --color --file schemas/core.openapi.yml
```

### VS Code setup

If you are running the VS Code Python extension, make sure to select the
correct interpreter.
Hit `Control` + `Shift` + `p`, type `Python: Select Interpreter` and select the
corresponding option. Select the correct python version (should be something
along the lines of `habits-tracker-py3.13`).

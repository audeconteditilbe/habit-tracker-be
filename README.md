
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
# Activate virtual environment
poetry shell
```

Alternatively, you can prefix any command with `poetry run`. For instance:
```bash
poetry run python manage.py runserver
```

You can deactivate the virtual environment with:
```bash
# Deactivate virtual env
exit
```

Or remove the virtual environment entirely (if needed):
```bash
# # Remove the virtual environment entirely (if needed):
# poetry env remove python
```

### Export dependencies

You can export the dependency list into a `requirements.txt` file with:
```bash
# Generate `requirements.txt` form poetry
poetry export -f requirements.txt --output requirements.txt
```

## Development

You can start the local development server with:
```bash
poetry run python manage.py runserver
```

### Code formatting / linting

You can format code by running:
```bash
poetry run black .
```

and linting with:

```bash
poetry run flake8 .
```

### VS Code setup

If you are running the VS Code Python extension, make sure to select the
correct interpreter.
Hit `Control` + `Shift` + `p`, type `Python: Select Interpreter` and select the
corresponding option. Select the correct python version (should be something
along the lines of `habits-tracker-py3.13`).
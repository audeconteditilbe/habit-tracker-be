# habit-tracker-be

Backend to my Habits Tracker project

## Setup

### Virtual env

If running for the first time, create a virtual environment:

```bash
# Create a virtual environment
python -m venv .venv
```

The virtual environment can be activated with:

```bash
# Activate the virtual environment
source .venv/bin/activate
```

### Install

Install dependencies:

```bash
pip install -r requirements.txt
```

## Development

### Installing new packages

Upon installing new packages, please update the dependencies list by running

```bash
pip freeze > requirements.txt
```

### Code formatting / linting

You can format code by running:

```bash
black .
```

and linting with:

```bash
flake8 .
```

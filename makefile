dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py migrate
makemigrations:
	poetry run python manage.py makemigrations
test:
	poetry run python manage.py test
black:
	poetry run black .
flake:
	poetry run flake8 .
schema:
	poetry run python manage.py spectacular --color --file schemas/core.openapi.yml


logs:
	docker compose logs -f

down:
	docker compose down --volumes

start:
	COMPOSE_BAKE=True poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

migration:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser

newapp:
	poetry run python manage.py startapp $(app)
	@# to execute run `make newapp app=cenas`

test:
	poetry run pytest -vvv

compose.createsuperuser:
	docker compose run --rm web poetry run python manage.py createsuperuser

compose.start:
	docker compose up --build --force-recreate

compose.migrate:
	docker compose run --rm web poetry run python manage.py migrate

compose.migration:
	docker compose run --rm web poetry run python manage.py makemigrations
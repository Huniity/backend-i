build:
	docker compose build

start: build
	COMPOSE_BAKE=True docker compose up -d --force-recreate

down:
	docker compsoe down --volumes

logs:
	docker compose logs -f

api-logs:
	docker compose logs -f api

test: build
	docker compose run --rm --entrypoint="" api poetry run pytest -vvv
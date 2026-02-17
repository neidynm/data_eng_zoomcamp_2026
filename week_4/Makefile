.PHONY: help build up down restart logs shell dbt-debug dbt-run dbt-test clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make build        Build Docker images"
	@echo "  make up           Start containers"
	@echo "  make down         Stop containers"
	@echo "  make restart      Restart containers"
	@echo "  make logs         View logs"
	@echo "  make shell        Open shell in dbt container"
	@echo "  make dbt-debug    Run dbt debug"
	@echo "  make dbt-run      Run dbt models"
	@echo "  make dbt-test     Run dbt tests"
	@echo "  make clean        Remove containers & DuckDB file"

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f

shell:
	docker compose run --rm dbt bash

dbt-debug:
	docker compose run --rm dbt dbt debug

dbt-run:
	docker compose run --rm dbt dbt run

dbt-test:
	docker compose run --rm dbt dbt test

clean:
	docker compose down -v
	rm -f duckdb.db

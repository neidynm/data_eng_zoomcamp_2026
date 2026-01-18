# -------------------------
# ENVIRONMENT
# -------------------------
ENV_FILE := .env

# -------------------------
# DOCKER COMMANDS
# -------------------------

## Build containers (images only)
build:
	docker compose build

## Start all services in foreground
up:
	docker compose up

## Start all services in detached mode
up-d:
	docker compose up -d

## Stop containers (keeps data volume)
down:
	docker compose down

## Stop and delete volumes (CAREFUL!)
down-v:
	docker compose down -v

## Tail logs from all services
logs:
	docker compose logs -f

## Restart services
restart:
	docker compose down
	docker compose up -d

# -------------------------
# ETL & UTILITIES
# -------------------------

## Run the ETL pipeline inside the container
run-etl:
	docker compose run --rm etl



## Run ETL wi

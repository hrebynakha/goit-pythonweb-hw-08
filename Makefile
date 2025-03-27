include .env

db:
	docker run --name hw08 -p 5432:5432 -e POSTGRES_PASSWORD=${DB_PASSWORD} -d postgres
migration:
	alembic revision --autogenerate -m 'Init'
migrate:
	alembic upgrade head
f:
	black . --exclude=venv
run:
	python main.py
up-f:
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	sudo docker-compose --env-file .env up -d
up:
	poetry export --without-hashes -f requirements.txt --output requirements.txt
	docker-compose --env-file .env up -d
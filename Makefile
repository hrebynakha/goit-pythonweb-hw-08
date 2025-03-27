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
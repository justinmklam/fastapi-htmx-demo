install:
	poetry install
	poetry env info

run:
	poetry run uvicorn src.main:app --reload

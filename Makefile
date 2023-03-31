install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

make lint:
	poetry run flake8 task_manager

run_test:
	poetry run pytest --cov=page_loader tests/ --cov-report xml
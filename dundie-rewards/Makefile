.PHONY: install lint fmt test watch clean run

install:
	@echo "Installing for dev environment"
	@pip install -e .

lint:
	@pflake8

fmt:
	@isort dundie tests integration
	@black dundie tests integration

test:
	@pytest -vv -s --forked

watch:
	@ptw -- -vv --forked

clean:            ## Clean unused files.
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build

run:
	@dundie load ./assets/people.csv
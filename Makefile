black: ## Black format every python file to line length 100
	find . -type f -name "*.py" | xargs black --line-length=100;
	find . -type f -name "*.py" | xargs absolufy-imports;
	make clean;

test: ## Run pytest for every test file
	pytest -W ignore -vv .;
	make clean;

flake8: ## Flake8 every python file
	find . -type f -name "*.py" -a | xargs flake8;

pylint: ## Pylint every python file
	find . -type f -name "*.py" -a | xargs pylint;

build: ## Build package distribution files
	flit build;

publish: ## Publish package distribution files to pypi
	flit publish;
	make clean;

clean: ## Remove caches, checkpoints, and distribution artifacts
	find . \( -name ".DS_Store" -o -name ".ipynb_checkpoints" -o -name "__pycache__" -o -name ".pytest_cache" \) | xargs rm -rf
	rm -rf dist/ build/ **/*.egg-info

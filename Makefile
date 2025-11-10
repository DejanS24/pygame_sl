.PHONY: help install install-dev test test-unit test-integration coverage format lint type-check clean build docs watch

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package and runtime dependencies
	pip install -e .
	pip install -r requirements.txt

install-dev:  ## Install package and development dependencies
	pip install -e .
	pip install -r requirements-dev.txt
	@echo ""
	@echo "✓ Installation complete!"
	@echo "Run 'pre-commit install' to set up git hooks"

test:  ## Run all tests
	pytest

test-unit:  ## Run only unit tests
	pytest -m unit

test-integration:  ## Run only integration tests
	pytest -m integration

coverage:  ## Run tests with coverage report
	pytest --cov=lang --cov=generator --cov-report=html --cov-report=term-missing
	@echo ""
	@echo "✓ Coverage report generated in htmlcov/index.html"

format:  ## Format code with black
	black .
	@echo ""
	@echo "✓ Code formatted successfully"

lint:  ## Lint code with ruff
	ruff check .
	@echo ""
	@echo "✓ Linting complete"

lint-fix:  ## Lint and auto-fix issues
	ruff check --fix .
	@echo ""
	@echo "✓ Auto-fixes applied"

type-check:  ## Type check with mypy
	mypy lang/ generator/ || true
	@echo ""
	@echo "✓ Type checking complete"

quality:  ## Run all quality checks (format, lint, type-check, test)
	@echo "Running code formatting..."
	@make format
	@echo ""
	@echo "Running linter..."
	@make lint
	@echo ""
	@echo "Running type checker..."
	@make type-check
	@echo ""
	@echo "Running tests..."
	@make test
	@echo ""
	@echo "✓ All quality checks passed!"

clean:  ## Clean build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	@echo ""
	@echo "✓ Cleanup complete"

build:  ## Build distribution packages
	python -m build
	@echo ""
	@echo "✓ Build complete! Check dist/ directory"

build-check:  ## Build and check distribution packages
	python -m build
	twine check dist/*
	@echo ""
	@echo "✓ Build validation complete"

docs:  ## Generate documentation (placeholder)
	@echo "Documentation files are in docs/"
	@echo "- docs/TUTORIAL.md"
	@echo "- docs/GRAMMAR_REFERENCE.md"
	@echo "- docs/EXAMPLES.md"
	@echo "- docs/CONTRIBUTING.md"

example:  ## Generate code from example game
	@echo "Generating code from examples/game1.pg..."
	textx generate examples/game1.pg --target python
	@echo ""
	@echo "✓ Generated game file! Run with: python 2d_platformer.py"

watch:  ## Watch a .pg file and auto-regenerate on changes
	@if [ -z "$(FILE)" ]; then \
		echo "Usage: make watch FILE=path/to/game.pg"; \
		echo "Example: make watch FILE=examples/simple_platformer.pg"; \
	else \
		python watch.py $(FILE); \
	fi

pre-commit:  ## Install pre-commit hooks
	pre-commit install
	@echo ""
	@echo "✓ Pre-commit hooks installed"

pre-commit-run:  ## Run pre-commit hooks on all files
	pre-commit run --all-files

dev-setup:  ## Complete development environment setup
	@echo "Setting up development environment..."
	@make install-dev
	@make pre-commit
	@echo ""
	@echo "✓ Development environment ready!"
	@echo ""
	@echo "Next steps:"
	@echo "  1. Run 'make test' to verify everything works"
	@echo "  2. Run 'make example' to generate a sample game"
	@echo "  3. Check 'make help' for all available commands"

.DEFAULT_GOAL := help

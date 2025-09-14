# Python Data Science Template

# Default recipe
default:
    @just --list --unsorted

# ==== Development ====

# Run tests with pytest
[group('development')]
test:
    PYTHONPATH=src/local_funcs/src uv run pytest -vv

# Format code with ruff
[group('development')]
fmt:
    uv run ruff format .
    uv run ruff check --fix .

# Lint code with ruff and ty
[group('development')]
lint:
    uv run ruff check .
    uv run ty check .

# ==== Scripts ====

# Run hello world script
[group('scripts')]
hello:
    uv run scripts/hello_world.py

# Run hello world script with custom numbers
[group('scripts')]
hello-custom *numbers:
    uv run scripts/hello_world.py --numbers {{numbers}}

# ==== Jupyter ====

# Start Jupyter Lab
[group('jupyter')]
lab:
    uv run jupyter lab

# Start Jupyter Notebook
[group('jupyter')]
notebook:
    uv run jupyter notebook

# ==== Testing ====

# Run tests with coverage
[group('testing')]
test-cov:
    PYTHONPATH=src/local_funcs/src uv run pytest --cov=local_funcs --cov-report=html --cov-report=term

# Run specific test file
[group('testing')]
test-file file:
    PYTHONPATH=src/local_funcs/src uv run pytest {{file}} -vv

# ==== Development Tools ====

# Install development dependencies (after conda env is activated)
[group('tools')]
setup:
    uv sync --dev

# Clean up temporary files
[group('tools')]
clean:
    rm -rf .pytest_cache/
    rm -rf __pycache__/
    rm -rf htmlcov/
    rm -rf .ipynb_checkpoints/
    find . -name "*.pyc" -delete
    find . -name "*.pyo" -delete
    find . -name "__pycache__" -type d -exec rm -rf {} +

# Clean data directories
[group('tools')]
clean-data:
    find data/tmp -type f -not -name ".gitignore" -delete
    find data/intermediate -type f -not -name ".gitignore" -delete

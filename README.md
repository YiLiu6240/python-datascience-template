# Python Data Science Template

A comprehensive Python data science project template with conda environment management and uv for Python package dependencies.

## Quick Start

1. **Create conda environment:**

   ```bash
   conda env create -f environment.yml
   conda activate python-datascience-template
   ```

2. **Install Python dependencies:**

   ```bash
   just setup
   ```

3. **Run example script:**

   ```bash
   just hello
   ```

4. **Start Jupyter Lab:**

   ```bash
   just lab
   ```

## Project Structure

- `src/local_funcs/`: Local utility package (installed as editable)
- `scripts/`: Analysis and processing scripts
- `notebooks/`: Jupyter notebooks for exploration
- `docs/`: Project documentation
- `data/`: Data storage with organized subdirectories
  - `raw/`: Original, immutable data
  - `intermediate/`: Processed data
  - `artifacts/`: Final outputs and models
  - `tmp/`: Temporary files
- `tests/`: Test suite

## Environment Management

This project uses a hybrid approach:

- **Conda** for system-level dependencies (Python, uv, just)
- **uv** for Python package management within the conda environment

See @DEV.md for detailed development instructions.

## Key Features

- Conda environment with minimal system dependencies
- Local `local_funcs` package for project utilities
- Organized data directory structure with proper gitignore
- Jupyter integration for interactive development
- Task runner with just for common operations
- Modern Python tooling (ruff, ty, pytest)


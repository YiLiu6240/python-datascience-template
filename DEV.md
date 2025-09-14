# Development Guide

This document provides instructions for setting up and developing the Python data science template.

## Setup

This project uses a hybrid environment management approach:

- **Conda** for system-level dependencies and Python version
- **uv** for Python package management within the conda environment

### Prerequisites

- Conda or Miniconda
- just task runner (installed via conda)

### Installation

```bash
# Create conda environment
conda env create -f environment.yml

# Activate environment
conda activate python-datascience-template

# Install Python dependencies
just setup
```

## Development Tasks

### Running Scripts

```bash
# Run hello world example
just hello

# Run with custom numbers
just hello-custom 10 20 30 40
```

### Jupyter Development

```bash
# Start Jupyter Lab (recommended)
just lab

# Start Jupyter Notebook
just notebook
```

### Test suite

```bash
# Run all tests
just test

# Run tests with coverage
just test-cov

# Run specific test file
just test-file tests/test_local_funcs.py
```

### Code Quality

```bash
# Format code
just fmt

# Run linters
just lint
```

### Cleanup

```bash
# Clean temporary files
just clean

# Clean data directories (tmp and intermediate)
just clean-data
```

## Project Structure

### Source Code

- `src/local_funcs/`: Local utility package installed as editable dependency
  - Configured as uv workspace member
  - Provides project-specific functions and utilities

### Data Organization

- `data/raw/`: Original, immutable data files
- `data/intermediate/`: Processed data files
- `data/artifacts/`: Final outputs, models, reports
- `data/tmp/`: Temporary files (cleaned regularly)

All data directories are configured with `.gitignore` to prevent accidental commits.

### Scripts vs Notebooks

- `scripts/`: Production scripts with argument parsing and proper structure
- `notebooks/`: Exploratory analysis and prototyping

## Environment Management Details

### Conda Environment (`environment.yml`)

- Python 3.13
- uv package manager
- just task runner

### Python Dependencies (`pyproject.toml`)

- **Development**: pytest, ruff, ty, jupyter
- **Data Science**: pandas, numpy, matplotlib, seaborn, scikit-learn
- **Local**: local_funcs package (workspace member)

### Workspace Configuration

The project uses uv workspace to manage the local `local_funcs` package:

```toml
[tool.uv.workspace]
members = ["src/local_funcs"]

[tool.uv.sources]
local-funcs = { workspace = true, editable = true }
```

## Development Dependencies

- **ruff**: Fast Python linter and formatter
- **ty**: Type checker for Python
- **pytest**: Testing framework
- **jupyter**: Interactive development environment

## Coding Style

This project follows the coding guidelines specified in the main repository. Key points:

- Use type annotations for all functions
- Include docstrings for public functions
- Follow PEP 8 style guidelines (enforced by ruff)
- Limit lines to 80 characters where practical
- Use ASCII printable characters only

## Data Science Workflow

1. **Data Ingestion**: Place raw data in `data/raw/`
2. **Exploration**: Use Jupyter notebooks for initial analysis
3. **Processing**: Create scripts in `scripts/` for reproducible processing
4. **Utilities**: Add reusable functions to `src/local_funcs/`
5. **Results**: Save outputs to `data/artifacts/`

## Testing

Write tests for utility functions in `src/local_funcs/`. Use pytest for testing:

```bash
# Run tests with proper PYTHONPATH
PYTHONPATH=src/local_funcs/src pytest -vv
```

The justfile handles the PYTHONPATH configuration automatically.


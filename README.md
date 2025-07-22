# Python Project Reference Template
A minimal best-practice template for python projects.
This is mainly a reference for myself, but feel free to use it as a starting point for your own projects.

# Tools
- `uv` for managing virtual envs, dependency management and packaging
- `ruff` for linting and formatting
- `mypy` for type checking
- `pytest` for testing
- `pdoc` for documentation
- `pre-commit` to enforce code quality
- `github actions` for CI/CD
- `python-semantic-release` for versioning

# Prerequisits

## Install uv
`uv` is an extremely fast Python package and project manager
https://docs.astral.sh/uv/getting-started/installation/

## Recommended VSCode Plugins:
- Python
- Ruff
- MyPy

## Clone repository

    git clone ...

# Usage

## Install dependencies

    uv sync --extra dev

## Install pre-commit hooks

    pre-commit install

## Run pre-commit hooks

    pre-commit run --all-files

## Run tests

    pytest
    pytest --testmon    # Only run tests affected by changes

# Versioning

This project uses semantic-release for versioning. Commit message convention:
https://www.conventionalcommits.org/en/v1.0.0/

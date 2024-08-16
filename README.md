# Python Project Reference Template
A minimal best-practice template for python projects.
This is mainly a reference for myself, but feel free to use it as a starting point for your own projects.

# Tools
- `pyenv` for managing python versions
- `poetry` for packaging and dependency management
- `ruff` for linting and formatting
- `mypy` for type checking
- `pytest` for testing
- `pdoc` for documentation
- `pre-commit` to enforce code quality
- `github actions` for CI/CD
- `python-semantic-release` for versioning

# Prerequisits

## Install pyenv
Pyenv is a tool that lets you manage multiple versions of python on your system.
https://github.com/pyenv/pyenv

## Install poetry
Poetry is a Python dependency management and packaging tool.
https://python-poetry.org/docs/

Set poetry to use in-project virtual environments:

    poetry config virtualenvs.in-project true

## Recommended VSCode Plugins:
- Python
- Ruff
- MyPy

## Clone repository

    git clone ...

# Usage

## Install dependencies

    poetry install

## Activate virtual environment

    poetry shell

## Install pre-commit hooks

    pre-commit install
    pre-commit install --hook-type commit-msg

## Run pre-commit hooks

    pre-commit run --all-files

## Run tests

    pytest
    pytest --testmon    # Only run tests affected by changes

# Versioning

This project uses semantic-release for versioning. Commit message convention:
https://www.conventionalcommits.org/en/v1.0.0/



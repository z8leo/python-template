import importlib.metadata

# Derives version dynamically from pyproject.toml
__version__ = importlib.metadata.version(__name__)

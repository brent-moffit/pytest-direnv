import pytest
from pytest_direnv.direnv import load_vars
import os


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    """Load environment variables from .envrc"""

    envrc_vars = load_vars()

    for var, val in envrc_vars.items():
        os.environ[var] = val

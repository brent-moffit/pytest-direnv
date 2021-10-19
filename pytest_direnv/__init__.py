import os

import pytest

from pytest_direnv.direnv import load_vars


@pytest.hookimpl(tryfirst=True)
def pytest_load_initial_conftests(args, early_config, parser):
    """Load environment variables from .envrc on pytest start"""

    envrc_vars = load_vars(dir=early_config.invocation_params.dir)

    for var, val in envrc_vars.items():
        os.environ.setdefault(var, val)

import os


def test_direnv_load():
    assert os.getenv("TEST_VAR") == "test value"

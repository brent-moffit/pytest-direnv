import os


def test__direnv_load():
    assert os.getenv("TEST_VAR") == "test value"

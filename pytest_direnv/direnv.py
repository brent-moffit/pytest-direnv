import subprocess


def load_vars() -> dict:
    result = subprocess.check_output(
        "direnv exec . python -m pytest_direnv.direnv_export",
        shell=True,
    )

    return eval(result)

import subprocess


def load_vars() -> dict:
    result = subprocess.check_output(
        "direnv exec . python -m pyenv_direnv.direnv_export",
        shell=True,
    )

    return eval(result)

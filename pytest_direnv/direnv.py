import subprocess
from pathlib import Path


def load_vars(dir: Path) -> dict:
    """Load environment vairables from .envrc in the given directory (or parent)"""
    print("Loading environment vairables from .envrc")

    try:
        result = subprocess.check_output(
            f'direnv exec "{dir}" python -m pytest_direnv.direnv_export',
            shell=True,
        )
    except subprocess.CalledProcessError as e:
        print(f'Error loading .envrc file from "{dir}". Is direnv installed?')
        print(e.output)

        raise e

    return eval(result)

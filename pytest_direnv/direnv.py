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
        if e.returncode == 127:
            print("direnv was not found, no .envrc will be loaded.")
        else:
            print(f"Error loading .envrc file from {dir}:")
            print(e.output)
            raise e

    return eval(result)

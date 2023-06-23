import json
import pathlib
import subprocess


def tokei(path):
    """Calculate Tokei statistics for path."""
    init_path = pathlib.Path(__file__)
    tokei_path = init_path.parent / 'binaries' / 'macos-latest' / 'tokei'
    command = [str(tokei_path), path, "--output", "json"]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"tokei failed: {result.stderr}")
    data = json.loads(result.stdout)
    return data


__title__ = 'tokei'
__version__ = '0.1.0'
__author__ = 'Grant Jenks'
__license__ = 'Apache 2.0'
__copyright__ = '2023, Grant Jenks'

from codecov_cli import __version__
from codecov_cli import main


def test_version():
    assert __version__ == "0.1.0"


def test_existing_commands():
    assert sorted(main.cli.commands.keys()) == [
        "create-commit",
        "create-report",
        "do-upload",
    ]
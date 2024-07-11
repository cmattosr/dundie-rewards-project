import pytest
from unittest.mock import patch

MARKER = """\
unit: Mark unit tests
high: Mark high priority tests
medium: Mark medium priority tests
low: Mark low priority tests
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tempdir(request):
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield

@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """For each test, create a new database file on tmpdir
    force database.py to use that filepath
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.test.json"))
    with patch("dundie.database.DATABASE_PATH", test_db):
        yield
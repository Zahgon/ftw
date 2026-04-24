from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

import pytest

from . import util
from .ruleset import Test


def get_testdata(rulesets, use_rulesets):
    """
    In order to do test-level parametrization (is this a word?), we have to
    bundle the test data from rulesets into tuples so py.test can understand
    how to run tests across the whole suite of rulesets
    """
    pass


def test_id(val):
    """
    Dynamically names tests, useful for when we are running dozens to hundreds
    of tests
    """
    pass


@pytest.fixture
def destaddr(request):
    """
    Destination address override for tests
    """
    pass


@pytest.fixture
def port(request):
    """
    Destination port override for tests
    """
    pass


@pytest.fixture
def protocol(request):
    """
    Destination protocol override for tests
    """
    pass


@pytest.fixture
def http_serv_obj():
    """
    Return an HTTP object listening on localhost port 80 for testing
    """
    pass


@pytest.fixture
def with_journal(request):
    """
    Return full path of the testing journal
    """
    pass


@pytest.fixture
def tablename(request):
    """
    Set table name for journaling
    """
    pass


def pytest_addoption(parser):
    """
    Adds command line options to py.test
    """
    pass


def pytest_generate_tests(metafunc):
    """
    Pre-test configurations, mostly used for parametrization
    """
    pass

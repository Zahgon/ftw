import datetime
import sqlite3

from dateutil import parser
import pytest

from . import errors
from . import http
from . import util


class TestRunner(object):
    """
    Runner that accepts stages of a test and verifies expected and actual
    responses
    @TODO
    Accept logger objects for assertions
    """
    def test_status(self, expected_status, actual_status):
        """
        Compares the expected output against actual output of test and stage
        In a separate function to make debugging easy with py.test
        """
        pass

    def test_log(self, lines, log_contains, negate):
        """
        Checks if a series of log lines contains a regex specified in the
        output stage. It will flag true on the first log_contains regex match
        and then assert on the flag at the end of the function
        """
        pass

    def test_response(self, response_object, regex):
        """
        Checks if the response response contains a regex specified in the
        output stage. It will assert that the regex is present.
        """
        pass

    def test_response_str(self, response, regex):
        """
        Checks if the response response contains a regex specified in the
        output stage. It will assert that the regex is present.
        """
        pass

    def query_for_stage_results(self, tablename):
        """
        Construct query for sqlite database for a specific stage
        run from a journal.
        Possible SQL injection here, but since its sqlite and if
        someone had control of the python script and the sqlite
        database, they can just open the database/modify it without
        using our program
        """
        pass

    def run_stage_with_journal(self, rule_id, test, journal_file,
                               tablename, logger_obj):
        """
        Compare entries and responses in a journal file with a
        logger object.
        This will follow similar logic as run_stage, where a
        logger_obj.get_logs() MUST be implemented by the user so
        times can be retrieved and compared against the responses
        logged in the journal db
        """
        pass

    def run_test_build_journal(self, rule_id, test, journal_file,
                               tablename, http_ua=None):
        """
        Build journal entries from a test within a specified rule_id
        Pass in the rule_id, test object, and path to journal_file
        DB MUST already be instantiated from util.instantiate_database()
        """
        pass

    def run_stage(self, stage, logger_obj=None, http_ua=None):
        """
        Runs a stage in a test by building an httpua object with the stage
        input, waits for output then compares expected vs actual output
        http_ua can be passed in to persist cookies
        """
        pass

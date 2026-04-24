import os
from glob import glob
import sqlite3

import yaml

from . import ruleset


def get_insert_statement(table_name):
    """
    Prepare SQL statement to be inserted into the FTW journal
    """
    pass


def instantiate_database(sqlite_file='ftwj.sqlite'):
    """
    Create journal database for FTW runs
    """
    pass


def get_rulesets(ruledir, recurse):
    """
    List of ruleset objects extracted from the yaml directory
    """
    pass


def get_files(directory, extension):
    """
    Take a directory and an extension and return the files
    that match the extension
    """
    pass


def extract_yaml(yaml_files):
    """
    Take a list of yaml_files and load them to return back
    to the testing program
    """
    pass


def ensure_str(s, encoding='utf-8', errors='strict'):
    # Optimization: Fast return for the common case.
    pass


def ensure_binary(s, encoding='utf-8', errors='strict'):
    pass

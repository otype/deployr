# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from deployrlib.globals.return_codes import OS_INVALID_ARGUMENT, OS_SUCCESS
from deployrlib.repositories.supervisorctl_repository import parse_supervisorctl_params, run_supervisorctl_command, supervisorctl_reread


def setup_func():
    """
        set up test fixtures
    """
    pass

def teardown_func():
    """
        tear down test fixtures
    """
    pass


def test_parse_supervisorctl_params():
    assert ['a', 'b', 'c'] == parse_supervisorctl_params([' a ', 'b ', '    c'])
    assert ['a', 'b', 'c'] == parse_supervisorctl_params(' a , b ,     c')
    assert {'a': 'b'} == parse_supervisorctl_params({'a': 'b'})


def test_run_supervisorctl_command_without_param():
    assert OS_INVALID_ARGUMENT == run_supervisorctl_command(None)


@DeprecationWarning
def test_supervisor_reread():
    """
        Not used anymore! We are using XML-RPC now!
    """
    assert OS_SUCCESS == supervisorctl_reread()

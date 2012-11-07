# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from ostools import OS_INVALID_ARGUMENT
from ostools import OS_SUCCESS
from supervisor_api.supervisorctl_api import parse_supervisorctl_params
from supervisor_api.supervisorctl_api import supervisorctl_reread
from supervisor_api.supervisorctl_api import run_supervisorctl_command


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


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

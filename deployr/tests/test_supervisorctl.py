# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from ostools import OS_SUCCESS, OS_INVALID_ARGUMENT
from supervisor.supervisorctl_api import parse_supervisorctl_params
from supervisor.supervisorctl_api import supervisorctl_reread
from supervisor.supervisorctl_api import run_supervisorctl_command


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


def test_supervisor_reread():
    assert OS_SUCCESS == supervisorctl_reread()

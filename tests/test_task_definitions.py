# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from deployrlib.globals.task_aliases import DEPLOY_TASK
from deployrlib.globals.task_aliases import DEPLOY_CONFIRMATION_TASK
from deployrlib.globals.task_aliases import UNDEPLOY_TASK
from deployrlib.globals.task_aliases import UNDEPLOY_CONFIRMATION_TASK


def setup_func():
    pass


def teardown_func():
    pass


def test_constants():
    assert 'DEPLOY' == DEPLOY_TASK
    assert 'DEPLOY_CONFIRMATION' == DEPLOY_CONFIRMATION_TASK
    assert 'UNDEPLOY' == UNDEPLOY_TASK
    assert 'UNDEPLOY_CONFIRMATION' == UNDEPLOY_CONFIRMATION_TASK

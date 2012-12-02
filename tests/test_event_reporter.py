# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
from app_deployr.models.deploy_message import DeployMessage
from deployrlib.stats.event_reporter import EventReporter


deploy_message = DeployMessage(
    api_id='zzzzzzzzzzzzzzzzzzzzzzzz',
    db_host='riak1.dev.apitrary.net',
    db_port=8098,
    genapi_version=1,
    log_level='debug',
    entities=['users', 'dogs'],
    api_key='yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
)


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_send():
    event_reporter = EventReporter()
    response = event_reporter.send(deploy_message)
    assert response.code == 201

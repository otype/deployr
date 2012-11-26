# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
from messagequeue.queue_settings import DEPLOY_ROUTING_KEY
from deploy_action.deploy_message import DeployMessage

deploy_message_dict = {
    'api_id': '88sdhv98shdvlh123',
    'db_host': 'riak1.apitrary.net',
    'db_port': 8098,
    'genapi_version': 1,
    'log_level': 'debug',
    'entities': ['users', 'dogs'],
    'api_key': 'aksdfj09sdfj0sdjf09sjd0jsdv0js0dvj'
}

deploy_message = DeployMessage(
    api_id='aoisdf8hjsd9vh8',
    db_host='riak1.apitrary.net',
    db_port=8098,
    genapi_version=1,
    log_level='debug',
    entities=['users', 'dogs'],
    api_key='aksdfj09sdfj0sdjf09sjd0jsdv0js0dvj'
)


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_deploy_message_dict():
    assert deploy_message.to_dict()['task_type'] == 'DEPLOY'


@with_setup(setup_func, teardown_func)
def test_deploy_message_json():
    assert deploy_message.to_json() != ''
    assert 'DEPLOY' in deploy_message.to_json()


@with_setup(setup_func, teardown_func)
def test_deploy_message_routing_key():
    assert deploy_message.routing_key == DEPLOY_ROUTING_KEY

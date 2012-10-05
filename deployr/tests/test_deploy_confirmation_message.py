# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE, DEPLOY_CONFIRMATION_ROUTING_KEY
from task.messages.deploy_confirmation_message import DeployConfirmationMessage

deploy_confirmation_message_dict = {
    'task_type': 'DEPLOY_CONFIRMATION',
    'api_id': '88sdhv98shdvlh123',
    'genapi_version': 1,
    'host': 'some.awesome.host',
    'port': 12345,
    'status': 1,
    'created_at': 1234566.1234
}

deploy_confirmation_message = DeployConfirmationMessage(
    api_id=deploy_confirmation_message_dict['api_id'],
    genapi_version=deploy_confirmation_message_dict['genapi_version'],
    host=deploy_confirmation_message_dict['host'],
    port=deploy_confirmation_message_dict['port'],
    status=deploy_confirmation_message_dict['status']
)


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_deploy_confirmation_message_dict():
    assert deploy_confirmation_message.to_dict()['task_type'] == 'DEPLOY_CONFIRMATION'


@with_setup(setup_func, teardown_func)
def test_deploy_confirmation_message_json():
    assert deploy_confirmation_message.to_json() != ''
    assert 'DEPLOY_CONFIRMATION' in deploy_confirmation_message.to_json()


@with_setup(setup_func, teardown_func)
def test_deploy_confirmation_message_exchange():
    assert deploy_confirmation_message.exchange == GENAPI_DEPLOYMENT_EXCHANGE


@with_setup(setup_func, teardown_func)
def test_deploy_confirmation_message_routing_key():
    assert deploy_confirmation_message.routing_key == DEPLOY_CONFIRMATION_ROUTING_KEY

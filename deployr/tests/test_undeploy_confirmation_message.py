# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
from settings.queue_settings import UNDEPLOY_CONFIRMATION_ROUTING_KEY
from task.messages.undeploy_confirmation_message import UndeployConfirmationMessage

undeploy_confirmation_message_dict = {
    'task_type': 'DEPLOY_CONFIRMATION',
    'api_id': '88sdhv98shdvlh123',
    'status': 1
}

undeploy_confirmation_message = UndeployConfirmationMessage(
    api_id=undeploy_confirmation_message_dict['api_id'],
    status=undeploy_confirmation_message_dict['status']
)


def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_undeploy_confirmation_message_dict():
    assert undeploy_confirmation_message.to_dict()['task_type'] == 'UNDEPLOY_CONFIRMATION'


@with_setup(setup_func, teardown_func)
def test_undeploy_confirmation_message_json():
    assert undeploy_confirmation_message.to_json() != ''
    assert 'DEPLOY_CONFIRMATION' in undeploy_confirmation_message.to_json()


@with_setup(setup_func, teardown_func)
def test_undeploy_confirmation_message_routing_key():
    assert undeploy_confirmation_message.routing_key == UNDEPLOY_CONFIRMATION_ROUTING_KEY

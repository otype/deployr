# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE, UNDEPLOY_ROUTING_KEY
from task.messages.undeploy_message import UndeployMessage

undeploy_message_dict = {
    'api_id': '88sdhv98shdvlh123',    
}

undeploy_message = UndeployMessage(
    api_id='aoisdf8hjsd9vh8'
)

def setup_func():
    pass


def teardown_func():
    pass


@with_setup(setup_func, teardown_func)
def test_undeploy_message_dict():
    assert undeploy_message.to_dict()['task_type'] == 'UNDEPLOY'


@with_setup(setup_func, teardown_func)
def test_undeploy_message_json():
    assert undeploy_message.to_json() != ''
    assert 'DEPLOY' in undeploy_message.to_json()


@with_setup(setup_func, teardown_func)
def test_undeploy_message_exchange():
    assert undeploy_message.exchange == GENAPI_DEPLOYMENT_EXCHANGE


@with_setup(setup_func, teardown_func)
def test_undeploy_message_routing_key():
    assert undeploy_message.routing_key == UNDEPLOY_ROUTING_KEY

# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import json
from nose.tools.nontrivial import with_setup
from deployrlib.globals.task_aliases import DEPLOY_TASK, UNDEPLOY_TASK
from deployrlib.models.errors import UnacceptableMessageException
from deployrlib.models.task_factory import TaskFactory


def setup_func():
    global deploy_message
    deploy_message = {
        'task_type': 'DEPLOY',
        'api_id': "88sdhv98shdvlh123",
        'db_host': 'db1.apitrary.net',
        'db_port': 8098,
        'genapi_version': 1,
        'log_level': 'debug',
        'entities': ['user', 'object', 'contact'],
        'api_key': 'iis9nd9vnsdvoijsdvoin9s8dv'
    }

    global undeploy_message
    undeploy_message = {
        "task_type": "UNDEPLOY",
        "api_id": "88sdhv98shdvlh123"
    }


def teardown_func():
    "tear down test fixtures"


def test_constructor_with_missing_task_type():
    modified_message = {
        "api_id": "88sdhv98shdvlh123",
        "db_host": "db1.apitrary.net",
        "db_port": 8098,
        "genapi_version": 1,
        "log_level": "debug",
        "entities": ["user", "object", "contact"],
        "api_key": "iis9nd9vnsdvoijsdvoin9s8dv"
    }

    try:
        task_factory = TaskFactory()
        task_factory.load_message(modified_message)
    except UnacceptableMessageException:
        return True
    except Exception:
        return False


@with_setup(setup_func, teardown_func)
def test_constructor_with_valid_message():
    task_factory = TaskFactory()
    task_factory.load_message(json.dumps(deploy_message))
    assert task_factory.task_type() == DEPLOY_TASK

    task_factory.load_message(json.dumps(undeploy_message))
    assert task_factory.task_type() == UNDEPLOY_TASK

    task = task_factory.get_task()
    assert task.api_id == undeploy_message['api_id']

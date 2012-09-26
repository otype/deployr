# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from messagequeue.errors import UnacceptableMessageException
from messagequeue.message_parser import parse_task_type

def setup_func():
    global message
    message = {
        "task_type": "DEPLOY",
        "api_id": "88sdhv98shdvlh123",
        "db_host": "db1.apitrary.net",
        "db_port": 8098,
        "genapi_version": 1,
        "log_level": "debug",
        "entities": [ "user", "object", "contact" ],
        "api_key": "iis9nd9vnsdvoijsdvoin9s8dv",
        "api_access_key": "jjjoindv08988v88dh"
    }


def teardown_func():
    "tear down test fixtures"


def test_parse_task_type_missing_task_type():
    message = {
        "api_id": "88sdhv98shdvlh123",
        "db_host": "db1.apitrary.net",
        "db_port": 8098,
        "genapi_version": 1,
        "log_level": "debug",
        "entities": [ "user", "object", "contact" ],
        "api_key": "iis9nd9vnsdvoijsdvoin9s8dv",
        "api_access_key": "jjjoindv08988v88dh"
    }

    try:
        parse_task_type(message)
    except UnacceptableMessageException:
        pass
    except Exception:
        return False


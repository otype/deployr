# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from actions.deploy_actions import deploy_api
from messagequeue.errors import UnacceptableMessageException
from messagequeue.errors import MissingAttributeException
from messagequeue.errors import UnknownTaskTypeException

##############################################################################
#
# helper functions
#
##############################################################################


def parse_deploy_message(incoming_message):
    """
        Parses an incoming message for all attributes.

        Message layout is:

        {
            “task_type”: ”DEPLOY”,
            “api_id”: “88sdhv98shdvlh123”,
            “db_host”: “db1.apitrary.net”,
            “db_port”: 8098,
            “genapi_version”: 1,
            “log_level”: “debug”,
            “entities”: [ “user”, “object”, “contact” ],
            “api_key”: “iis9nd9vnsdvoijsdvoin9s8dv”,
            “api_access_key”: “jjjoindv08988v88dh”
        }

        Only if all attributes have been provided, we will
        pass on to the next step: deploy.
    """
    attribute_list = ['task_type', 'api_id', 'db_host', 'db_port', 'genapi_version',
                      'log_level', 'entities', 'api_key', 'api_access_key']
    for item in attribute_list:
        if item not in incoming_message:
            raise MissingAttributeException('Missing attribute {} in message.'.format(item))

    # call the deploy action
    deploy_api(
        api_id=incoming_message['api_id'],
        db_host=incoming_message['db_host'],
        genapi_version=incoming_message['genapi_version'],
        log_level=incoming_message['log_level'],
        entities=incoming_message['entities']
    )


def parse_task_type(incoming_message):
    """
        Get the task type from the given message
    """
    if 'task_type' not in incoming_message:
        raise UnacceptableMessageException('Missing task type in message')

    task_type = incoming_message['task_type']
    if task_type.upper() == 'DEPLOY':
        parse_deploy_message(incoming_message)
    else:
        raise UnknownTaskTypeException('Task type {} is unknown.'.format(task_type.upper()))


##############################################################################
#
# main call methods
#
##############################################################################


def parse_message(incoming_message):
    """
        Parse an incoming message for task type. Call the appropriate action.
    """
    try:
        parse_task_type(incoming_message)
    except UnacceptableMessageException, e:
        log.error(e)
    except UnknownTaskTypeException, e:
        log.error(e)

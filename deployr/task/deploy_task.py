# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from actions.deploy import deploy_api
from errors.exception_definitions import InvalidTaskTypeException


class DeployTask(object):
    """
        Deploy task definition
    """

    def __init__(self, message):
        """
            Initialize the Deploy task
        """
        self.message = message
        if not self.is_valid_deploy_message():
            log.error('Task type {} is unknown.'.format(self.task_type()))
            raise InvalidTaskTypeException('Task type {} is unknown.'.format(self.task_type()))

        # parse the message for necessary parameters
        self.parse_parameters()

    def task_type(self):
        """
            Parse the message and read the task type
        """
        return self.message['task_type'].upper()

    def parse_parameters(self):
        """
            Read out all parameters needed to run the deploy task
        """
        self.api_id = self.message['api_id']
        self.db_host = self.message['db_host']
        self.genapi_version = self.message['genapi_version']
        self.log_level = self.message['log_level']
        self.entities = self.message['entities']

    def is_valid_deploy_message(self):
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
                “api_key”: “iis9nd9vnsdvoijsdvoin9s8dv”
            }

            Only if all attributes have been provided, we will
            pass on to the next step: deploy.
        """
        attribute_list = ['task_type', 'api_id', 'db_host', 'db_port', 'genapi_version', 'log_level',
                          'entities', 'api_key']
        for item in attribute_list:
            if item not in self.message:
                log.warning('Missing attribute {} in message.'.format(item))
                return False

        return True

    def run(self):
        """
            Hooked-up method to run when deploying an API
        """
        return deploy_api(
            api_id=self.api_id,
            db_host=self.db_host,
            genapi_version=self.genapi_version,
            log_level=self.log_level,
            entities=self.entities
        )

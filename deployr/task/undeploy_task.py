# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from actions.deploy_actions import undeploy_api
from errors.exception_definitions import InvalidTaskTypeException


class UndeployTask(object):
    """
        Undeploy task definition
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

    def is_valid_deploy_message(self):
        """
            Parses an incoming message for all attributes.

            Message layout is:

            {
                “task_type”: ”UNDEPLOY”,
                “api_id”: “88sdhv98shdvlh123”
            }

            Only if all attributes have been provided, we will
            pass on to the next step: deploy.
        """
        attribute_list = ['task_type', 'api_id']
        for item in attribute_list:
            if item not in self.message:
                log.warning('Missing attribute {} in message.'.format(item))
                return False

        return True

    def run(self):
        """
            Hooked-up method to run when undeploying an API
        """
        return undeploy_api(api_id=self.api_id)

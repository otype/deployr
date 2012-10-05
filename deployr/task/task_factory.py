# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import json
from pika import log
from errors.exception_definitions import UnacceptableMessageException
from errors.exception_definitions import InvalidTaskTypeException
from task.task_types.deploy_task import DeployTask
from settings.task_settings import DEPLOY_TASK
from settings.task_settings import UNDEPLOY_TASK
from task.task_types.undeploy_task import UndeployTask


class TaskFactory(object):
    """
        A generic task as basis for all task type classes
    """

    def load_message(self, message):
        """
           Loads the message.

           Will throw ValueError if this is no valid JSON
        """
        self.message = json.loads(message)

        # Validate the task! This fails if it's not a valid task.
        self.validate_task()

    def get_task(self):
        """
            Create the corresponding task object
        """
        try:
            if self.task_type() == DEPLOY_TASK:
                return DeployTask(self.message)
            elif self.task_type() == UNDEPLOY_TASK:
                return UndeployTask(self.message)
        except InvalidTaskTypeException, e:
            log.error('Could not create a valid task! Error: {}'.format(e))
            return None
        except TypeError, e:
            log.error('Task type is not identifiable! Error: {}'.format(e))
            return None

    def validate_task(self):
        """
            Is the incoming message a valid task?
        """
        if 'task_type' not in self.message:
            log.error('Missing task type in message: {}'.format(self.message))
            raise UnacceptableMessageException('Missing task type in message')

        log.debug('Valid task of type: {}'.format(self.task_type()))

    def task_type(self):
        """
            Parse the message and read the task type
        """
        return self.message['task_type'].upper()

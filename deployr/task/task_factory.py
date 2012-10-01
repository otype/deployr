# -*- coding: utf-8 -*-
"""

    <application_name>
    
    Copyright (c) 2012 apitrary

"""
import json
from pika import log
from messagequeue.errors import UnacceptableMessageException
from messagequeue.errors import InvalidTaskTypeException
from task.deploy_task import DeployTask
from task.task_definitions import DEPLOY_TASK
from task.task_definitions import UNDEPLOY_TASK
from task.undeploy_task import UndeployTask


class TaskFactory(object):
    """
        A generic task as basis for all task type classes
    """

    def __init__(self, message):
        """
            Setup the basic task object
        """
        # will throw ValueError
        self.message = json.loads(message)

        if not self._is_valid_task():
            log.error('Missing task type in message: {}'.format(self.message))
            raise UnacceptableMessageException('Missing task type in message')


    def create_task(self):
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


    def _is_valid_task(self):
        """
            Is the incoming message a valid task?
        """
        if 'task_type' not in self.message:
            return False
        else:
            return True


    def task_type(self):
        """
            Parse the message and read the task type
        """
        return self.message['task_type'].upper()

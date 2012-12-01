# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import json
from deployr.deployrlib.services.logging_service import get_logger as logger
from app_deployr.models.deploy_task import DeployTask
from app_deployr.models.undeploy_task import UndeployTask
from deployrlib.globals.task_aliases import DEPLOY_TASK, UNDEPLOY_TASK, LOADBALANCE_UPDATE_TASK
from deployrlib.models.errors import InvalidTaskTypeException, UnacceptableMessageException
from deployrlib.services import deployr_config_service
from lb_deployr.models.loadbalance_update_task import LoadbalanceUpdateTask


class TaskFactory(object):
    """
        A generic task as basis for all task type classes
    """

    def __init__(self):
        """
            We need the configuration upon task creation
        """
        self.config = deployr_config_service.load_configuration()

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
                return DeployTask(self.message, self.config)
            elif self.task_type() == UNDEPLOY_TASK:
                return UndeployTask(self.message, self.config)
            elif self.task_type() == LOADBALANCE_UPDATE_TASK:
                return LoadbalanceUpdateTask(self.message, self.config)
        except InvalidTaskTypeException, e:
            logger.error('Could not create a valid task! Error: {}'.format(e))
            return None
        except TypeError, e:
            logger.error('Task type is not identifiable! Error: {}'.format(e))
            return None

    def validate_task(self):
        """
            Is the incoming message a valid task?
        """
        if 'task_type' not in self.message:
            logger.error('Missing task type in message: {}'.format(self.message))
            raise UnacceptableMessageException('Missing task type in message')

        logger.debug('Valid task of type: {}'.format(self.task_type()))

    def task_type(self):
        """
            Parse the message and read the task type
        """
        return self.message['task_type'].upper()

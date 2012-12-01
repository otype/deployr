# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from deployr.deployrlib.services.logging_service import get_logger as logger
from deployrlib.globals.return_codes import OS_SUCCESS, OS_ERROR
from deployrlib.models.errors import UnacceptableMessageException, InvalidTaskTypeException
from deployrlib.models.task_factory import TaskFactory


def run_task(message):
    """
        Run the task from the given message
    """
    try:
        # create the task factory
        task_factory = TaskFactory()

        # check if we have a valid task
        task_factory.load_message(message)

        # get the task object
        task = task_factory.get_task()

        logger.info('Running task: {}'.format(task_factory.message))
        status = task.run()
        logger.info('Task status: {}'.format(status))

        # Send out the confirmation message
        logger.info('Confirming task execution for API: {}'.format(task.api_id))
        task.send_confirmation()

        return OS_SUCCESS
    except UnacceptableMessageException, e:
        logger.error('Could not create task factory for spawning tasks! Error: {}'.format(e))
        return OS_ERROR
    except InvalidTaskTypeException, e:
        logger.error(e)
        return OS_ERROR
    except AttributeError, e:
        logger.error(e)
        return OS_ERROR

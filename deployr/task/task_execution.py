# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from ostools import OS_ERROR, OS_SUCCESS
from task.task_factory import TaskFactory
from errors.exception_definitions import UnacceptableMessageException
from errors.exception_definitions import InvalidTaskTypeException


##############################################################################
#
# main call methods
#
##############################################################################


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

        log.info('Running task: {}'.format(task_factory.message))
        status = task.run()

        # Send out the confirmation message
        log.info('Confirming task execution for API: {}'.format(task.api_id))
        task.send_confirmation()

        return OS_SUCCESS
    except UnacceptableMessageException, e:
        log.error('Could not create task factory for spawning tasks! Error: {}'.format(e))
        return OS_ERROR
    except InvalidTaskTypeException, e:
        log.error(e)
        return OS_ERROR
    except AttributeError, e:
        log.error(e)
        return OS_ERROR

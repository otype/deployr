# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from errors import UnacceptableMessageException
from errors import InvalidTaskTypeException
from ostools import OS_ERROR, OS_SUCCESS
from task.task_factory import TaskFactory


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
        log.info('Task status: {}'.format(status))

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

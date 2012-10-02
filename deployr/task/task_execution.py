# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from ostools import OS_ERROR
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
        task_factory = TaskFactory(message)
        log.info('Running task: {}'.format(task_factory.message))

        task = task_factory.create_task()
        log.info("Identified task type: {}".format(task.task_type()))

        return task.run()

    except UnacceptableMessageException, e:
        log.error('Could not create task factory for spawning tasks! Error: {}'.format(e))
        return OS_ERROR
    except InvalidTaskTypeException, e:
        log.error(e)
        return OS_ERROR

# -*- coding: utf-8 -*-
"""

    <application_name>
    
    Copyright (c) 2012 apitrary

"""
from pika import log
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
    task_factory = TaskFactory(message)
    log.info('Running task: {}'.format(task_factory.message))

    task = task_factory.create_task()
    log.info("Identified task type: {}".format(task.task_type()))

    return task.run()


# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 27.11.12, 00:27 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import task_repository

def run_task(message):
    """
        Run the task from the given message
    """
    return task_repository.run_task(message=message)
# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 26.11.12, 23:58 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import supervisorctl_repository

def supervisorctl_reread():
    """
        Reread the supervisor_api configuration files
    """
    return supervisorctl_repository.supervisorctl_reread()


def supervisorctl_start(app_name):
    """
        Start given application via supervisor_api
    """
    return supervisorctl_repository.supervisorctl_start(app_name=app_name)


def supervisorctl_stop(app_name):
    """
        Stop given application via supervisor_api
    """
    return supervisorctl_repository.supervisorctl_stop(app_name=app_name)


def supervisorctl_restart(app_name):
    """
        Start given application via supervisor_api
    """
    return supervisorctl_repository.supervisorctl_restart(app_name=app_name)


def supervisorctl_add(app_name):
    """
        Add new application to supervisor_api configuration
    """
    return supervisorctl_repository.supervisorctl_add(app_name=app_name)


def supervisorctl_status(app_name):
    """
        Request status of given application
    """
    return supervisorctl_repository.supervisorctl_status(app_name=app_name)


def supervisorctl_remove(app_name):
    """
        Remove application from supervisor_api context
    """
    return supervisorctl_repository.supervisorctl_remove(app_name=app_name)
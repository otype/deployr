# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import os
import sys
from pika import log
from ostools import execute_shell_command
from ostools import OS_INVALID_ARGUMENT
from ostools import OS_CANNOT_INVOKE_COMMAND_ERROR


##############################################################################
#
# GLOBALS
#
##############################################################################


# the executable for calling supervisorctl
if sys.platform == 'darwin':
    # Do nothing! Mac ain't got no supervisor! We are just faking it here.
    SUPERVISORCTL = 'supervisorctl'
elif sys.platform == 'linux2':
    SUPERVISORCTL = '/usr/bin/supervisorctl'
else:
    SUPERVISORCTL = 'supervisorctl'

# All supervisord commands as strings
SUPERVISORCTL_START = 'start'
SUPERVISORCTL_STOP = 'stop'
SUPERVISORCTL_RESTART = 'restart'
SUPERVISORCTL_ADD = 'add'
SUPERVISORCTL_REMOVE = 'remove'
SUPERVISORCTL_STATUS = 'status'
SUPERVISORCTL_REREAD = 'reread'

# The whole set of supervisord commands
SUPERVISORCTL_COMMAND_LIST = [
    SUPERVISORCTL_START, SUPERVISORCTL_STOP, SUPERVISORCTL_RESTART,
    SUPERVISORCTL_ADD, SUPERVISORCTL_REMOVE, SUPERVISORCTL_STATUS,
    SUPERVISORCTL_REREAD
]

##############################################################################
#
# HELPER FUNCTIONS
#
##############################################################################


def parse_supervisorctl_params(params):
    """
        subprocess.call is a bit picky with the argument list. For this, we need
        to make sure that we don't pass in empty strings and we don't pass in strings
        with whitespaces.

        Make a few checks on the params list:
            - if it's a string as csv, run split() on it and strip() all elements
            - if it's a list, strip all elements

        Otherwise just return the params back.
    """
    if type(params) == str:
        return [element.strip() for element in params.split(',')]

    if type(params) == list:
        return [element.strip() for element in params]

    return params


def run_supervisorctl_command(command, params=None):
    """
        Reread the supervisor_api configuration files
    """
    if command is None:
        log.error('Missing supervisorctl command as parameter!')
        return OS_INVALID_ARGUMENT

    # all supervisorctl commands are lower case ... just in case:
    command = command.lower().split()

    # check if command is an acceptable one ...
    if command[0] not in SUPERVISORCTL_COMMAND_LIST:
        log.error('Unknown supervisorctl command: {}'.format(command))
        return OS_CANNOT_INVOKE_COMMAND_ERROR

    if params:
        checked_params = parse_supervisorctl_params(params)
        log.debug('Adding command params: {}'.format(checked_params))
        command += checked_params

    log.debug('Running supervisorctl command: {}'.format(command))
    return execute_shell_command([SUPERVISORCTL] + command)


##############################################################################
#
# API CALLS
#
##############################################################################

def supervisorctl_reread():
    """
        Reread the supervisor_api configuration files
    """
    log.debug('SUPERVISORCTL: Reread the supervisor_api configurations files')
    return run_supervisorctl_command(SUPERVISORCTL_REREAD)


def supervisorctl_start(app_name):
    """
        Start given application via supervisor_api
    """
    log.debug('SUPERVISORCTL: Requesting start of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_START, app_name)


def supervisorctl_stop(app_name):
    """
        Stop given application via supervisor_api
    """
    log.debug('SUPERVISORCTL: Requesting stop of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_STOP, app_name)


def supervisorctl_restart(app_name):
    """
        Start given application via supervisor_api
    """
    log.debug('SUPERVISORCTL: Requesting restart of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_RESTART, app_name)


def supervisorctl_add(app_name):
    """
        Add new application to supervisor_api configuration
    """
    log.debug('SUPERVISORCTL: Requesting addition of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_ADD, app_name)


def supervisorctl_status(app_name):
    """
        Request status of given application
    """
    log.debug('SUPERVISORCTL: Requesting status of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_STATUS, app_name)


def supervisorctl_remove(app_name):
    """
        Remove application from supervisor_api context
    """
    log.debug('SUPERVISORCTL: Requesting removal of application: {}'.format(app_name))
    return run_supervisorctl_command(SUPERVISORCTL_REMOVE, app_name)
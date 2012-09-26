# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from ostools import execute_shell_command
from ostools import OS_INVALID_ARGUMENT
from ostools import OS_CANNOT_INVOKE_COMMAND_ERROR


##############################################################################
#
# GLOBALS
#
##############################################################################


#SUPERVISORCTL = 'supervisorctl'
SUPERVISORCTL = '/Users/hgschmidt/bin/supervisorctl'


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
        Reread the supervisor configuration files
    """
    if command is None:
        log.error('Missing supervisorctl command as parameter!')
        return OS_INVALID_ARGUMENT

    # all supervisorctl commands are lower case ... just in case:
    command = command.lower()

    # check if command is an acceptable one ...
    if command not in ['reread', 'start', 'stop', 'restart', 'add', 'status']:
        log.error('Unknown supervisorctl command: {}'.format(command))
        return OS_CANNOT_INVOKE_COMMAND_ERROR

    if params:
        checked_params = parse_supervisorctl_params(params)
        log.debug('Adding command params: {}'.format(checked_params))
        command += checked_params

    log.debug('Running supervisorctl command: {}'.format(command))
    return execute_shell_command([SUPERVISORCTL] + command.split())


##############################################################################
#
# MAIN FUNCTIONS
#
##############################################################################

def supervisor_reread():
    """
        Reread the supervisor configuration files
    """
    log.info('Reread the supervisor configurations files')
    return run_supervisorctl_command('reread')


def supervisor_start(app_name):
    """
        Start given application via supervisor
    """
    log.info('Requesting start of application: {}'.format(app_name))
    return run_supervisorctl_command('start', app_name)


def supervisor_stop(app_name):
    """
        Stop given application via supervisor
    """
    log.info('Requesting stop of application: {}'.format(app_name))
    return run_supervisorctl_command('stop', app_name)


def supervisor_restart(app_name):
    """
        Start given application via supervisor
    """
    log.info('Requesting restart of application: {}'.format(app_name))
    return run_supervisorctl_command('restart', app_name)


def supervisor_add(app_name):
    """
        Add new application to supervisor configuration
    """
    log.info('Requesting addition of application: {}'.format(app_name))
    return run_supervisorctl_command('add', app_name)


def supervisor_status(app_name):
    """
        Request status of given application
    """
    log.info('Requesting status of application: {}'.format(app_name))
    return run_supervisorctl_command('status', app_name)


def supervisor_remove(app_name):
    """
        Remove application from supervisor context
    """
    log.info('Requesting removal of application: {}'.format(app_name))
    return run_supervisorctl_command('remove', app_name)
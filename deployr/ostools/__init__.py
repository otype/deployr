# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import subprocess
from pika import log

##############################################################################
#
# GLOBALS
#
##############################################################################


OS_SUCCESS = 0
OS_ERROR = 1
OS_MISUSE_ERROR = 2
OS_CANNOT_INVOKE_COMMAND_ERROR = 126
OS_COMMAND_NOT_FOUND_ERROR = 127
OS_INVALID_ARGUMENT = 128


##############################################################################
#
# FUNCTIONS
#
##############################################################################


def execute_shell_command(command):
    """
        Execute a single shell command. The command parameter needs to have
        all shell command parameters included, all in one array. E.g.:

        ['ls', '-l', '-a']

        No empty strings as parameter allowed!
    """
    try:
        return subprocess.call(command)
    except OSError, e:
        log.error('Had trouble executing command: {}! Error: {}'.format(command, e))
        return OS_ERROR


def write_file(filename, content):
    """
        Write a given content to a file with given filename.
    """
    with open(filename, 'w') as f:
        f.write(content)
        f.write('\n')

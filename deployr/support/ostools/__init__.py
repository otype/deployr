# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import socket
import subprocess
from config.logging_configuration import logger as log

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


def get_host_name():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(('google.com', 9))
        client = s.getsockname()[0]
    except socket.error:
        client = "Unknown IP"
    finally:
        del s
    return client


def get_open_port():
    """
        Responsible for getting a free port.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    log.debug('Port {} is available.'.format(port))
    return port


def get_local_public_ip_address():
    """
        Get the public IP address for this host
    """
    ipaddr = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 8000))
        ipaddr = s.getsockname()[0]
        s.close()
    except:
        pass

    return ipaddr

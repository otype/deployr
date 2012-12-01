# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 26.11.12, 22:38 CET
    
    Copyright (c) 2012 apitrary

"""
from deployr.deployrlib.services.logging_service import get_logger as logger
import subprocess
import os
import sys
from deployrlib.globals.return_codes import OS_ERROR

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
        logger.error('Had trouble executing command: {}! Error: {}'.format(command, e))
        return OS_ERROR


def python_interpreter_path():
    """
        Get the full path to the Python interpreter used here in deployr
    """
    return sys.executable


def which(program):
    """
        Works like shell's 'which'
    """

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None
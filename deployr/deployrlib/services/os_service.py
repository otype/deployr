# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 26.11.12, 22:39 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import os_repository

def execute_shell_command(command):
    """
        Execute a single shell command. The command parameter needs to have
        all shell command parameters included, all in one array. E.g.:

        ['ls', '-l', '-a']

        No empty strings as parameter allowed!
    """
    return os_repository.execute_shell_command(command=command)


def python_interpreter_path():
    """
        Get the full path to the Python interpreter used here in deployr
    """
    return os_repository.python_interpreter_path()


def which(program):
    """
        Works like shell's 'which'
    """
    return os_repository.which(program=program)
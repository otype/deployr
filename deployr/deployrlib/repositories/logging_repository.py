# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 26.11.12, 23:40 CET
    
    Copyright (c) 2012 apitrary

"""
import logging
from deployrlib.models.log_levels import LOGGING_LEVEL

def get_log_level_from_config(log_level):
    """
        Sets the log level (use colored logging output).
        This is a wrapper for python logging.
    """
    level = log_level.upper()
    if level == LOGGING_LEVEL.CRITICAL:
        return logging.CRITICAL
    if level == LOGGING_LEVEL.WARN:
        return logging.WARN
    if level == LOGGING_LEVEL.WARNING:
        return logging.WARN
    if level == LOGGING_LEVEL.DEBUG:
        return logging.DEBUG
    if level == LOGGING_LEVEL.ERROR:
        return logging.ERROR
    else:
        return logging.INFO


def setup_logging(log_level=None):
    """
        Configure logging
    """
    if log_level is None:
        log_level = logging.DEBUG

    # Initial config for logging
    logging.basicConfig()

    # Set logger name to 'deployr
    log = logging.getLogger('deployr')

    # Set the default log level
    log.setLevel(log_level)

    return log

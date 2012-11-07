# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import logging

##############################################################################
#
# FUNCTIONS
#
##############################################################################

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


def setup_logging():
    """
        Configure logging
    """
    # Initial config for logging
    logging.basicConfig()

    # Set logger name to 'deployr
    log = logging.getLogger('deployr')

    # Set the default log level
    log.setLevel(logging.DEBUG)

    return log

##############################################################################
#
# CONFIG CLASS (ENUM)
#
##############################################################################

class LOGGING_LEVEL:
    """
        Accepted log levels for log
    """
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARN = 'WARNING'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

##############################################################################
#
# GLOBAL CONFIG OBJECTS
#
##############################################################################

# LOGGER (setting default name to 'deployr')
#
#
logger = setup_logging()

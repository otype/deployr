# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 27.11.12, 01:14 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import logging_repository

def get_log_level_from_config(log_level):
    """
        Sets the log level (use colored logging output).
        This is a wrapper for python logger.
    """
    return logging_repository.get_log_level_from_config(log_level=log_level)


def setup_logging(log_level, file_writing_enabled):
    """
        Configure logging
    """
    return logging_repository.setup_logging(log_level=log_level, file_writing_enabled=file_writing_enabled)


def get_logger(log_level=None):
    """
        Get the logger object
    """
    return logging_repository.get_logger(log_level=log_level)
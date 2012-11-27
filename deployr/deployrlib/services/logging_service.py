# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 27.11.12, 01:14 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import logging_repository

def get_log_level_from_config(log_level):
    """
        Sets the log level (use colored logging output).
        This is a wrapper for python logging.
    """
    return logging_repository.get_log_level_from_config(log_level=log_level)


def setup_logging(log_level):
    """
        Configure logging
    """
    return logging_repository.setup_logging(log_level=log_level)

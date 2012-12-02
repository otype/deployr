# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 23:24 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import deployr_config_repository

def strip_out_sensitive_data(configuration_object):
    """
        Strip out all passwords from config hash
    """
    return deployr_config_repository.strip_out_sensitive_data(configuration_object=configuration_object)


def get_config_file():
    """
        Define the configuration file (and path)
    """
    return deployr_config_repository.get_deployr_config_file()


def load_configuration():
    """
        Loading configuration file
    """
    return deployr_config_repository.load_configuration()


def write_configuration(config_env):
    """
        Write the configuration file for the given environment
    """
    return deployr_config_repository.write_configuration(config_env=config_env)

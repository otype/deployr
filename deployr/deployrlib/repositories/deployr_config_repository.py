# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 23:21 CET
    
    Copyright (c) 2012 apitrary

"""
import shutil
import os
import sys
from deployrlib.config.environment_config import GLOBAL_CONF
from deployrlib.models.config_manager import ConfigManager
from deployrlib.models.environments import ENVIRONMENT

def strip_out_sensitive_data(configuration_object):
    """
        Strip out all passwords from config hash
    """
    config_to_show = str(configuration_object)
    config_to_show = config_to_show.replace(configuration_object['BROKER_PASSWORD'], '<hidden>')
    config_to_show = config_to_show.replace(configuration_object['SUPERVISOR_XML_RPC_USERNAME'], '<hidden>')
    config_to_show = config_to_show.replace(configuration_object['SUPERVISOR_XML_RPC_PASSWORD'], '<hidden>')

    return config_to_show


def get_deployr_config_file():
    """
        Define the configuration file (and path)
    """
    if sys.platform == 'darwin':
        config_file = "{}/.deployr/deployr.conf".format(os.getenv("HOME"))
    elif sys.platform == 'linux2':
        config_file = "/etc/deployr/deployr.conf"
    else:
        config_file = "{}/.deployr/deployr.conf".format(os.getenv("HOME"))

    return config_file


def load_configuration():
    """
        Loading configuration file
    """
    config_file = get_deployr_config_file()
    config_manager = ConfigManager(config_file)
    config_manager.setup_config_dir()

    if not os.path.exists(config_file):
        config_manager.load_config(config_obj=GLOBAL_CONF[ENVIRONMENT.DEV])
        config_manager.write_config()

    config_manager.load_config_from_file()
    return config_manager.config


def write_configuration(config_env):
    """
        Write the configuration file for the given environment
    """
    config_file = get_deployr_config_file()

    # Store existing config to <name>.backup
    if os.path.exists(config_file):
        shutil.move(config_file, "{}.backup".format(config_file))

    config_manager = ConfigManager(config_file)
    config_manager.setup_config_dir()
    config_manager.load_config(config_obj=GLOBAL_CONF[config_env])
    config_manager.write_config()

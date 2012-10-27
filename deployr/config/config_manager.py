# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import shutil
import os
import sys
from configobj import ConfigObj
from pika import log
from config.default_configuration import GLOBAL_CONF, ENVIRONMENT
from ostools import OS_SUCCESS

##############################################################################
#
# FUNCTIONS
#
##############################################################################

def strip_out_sensitive_data(configuration_object):
    """
        Strip out all passwords from config hash
    """
    config_to_show = str(configuration_object)
    config_to_show = config_to_show.replace(configuration_object['BROKER_PASSWORD'], '<hidden>')
    config_to_show = config_to_show.replace(configuration_object['SUPERVISOR_XML_RPC_USERNAME'], '<hidden>')
    config_to_show = config_to_show.replace(configuration_object['SUPERVISOR_XML_RPC_PASSWORD'], '<hidden>')

    return config_to_show


def get_config_file():
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
    config_file = get_config_file()
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
    config_file = get_config_file()

    # Store existing config to <name>.backup
    if os.path.exists(config_file):
        shutil.move(config_file, "{}.backup".format(config_file))

    config_manager = ConfigManager(config_file)
    config_manager.setup_config_dir()
    config_manager.load_config(config_obj=GLOBAL_CONF[config_env])
    config_manager.write_config()


##############################################################################
#
# CLASSES
#
##############################################################################

class ConfigManager(object):
    """
        The config manager supports loading and writing the deployr configuration
        file. This config file is required to load the necessary credentials and
        contacting node names.
    """

    def __init__(self, config_file='/etc/deployr/deployr.conf'):
        """
            Pre-load the configuration file name
        """
        self.config_file = config_file

    def load_config_from_file(self, config_file=None):
        """
            Load a configuration file
        """
        if config_file:
            self.config_file = config_file

        log.info("Setting configuration file {}".format(self.config_file))
        if not os.path.exists(self.config_file):
            log.error("Cannot load configuration file {}: not found!".format(self.config_file))
            sys.exit(1)

        try:
            self.config = ConfigObj(self.config_file)
        except Exception, e:
            log.error("Error on reading configuration file {}! Error: {}".format(self.config_file, e))
            sys.exit(1)

        return OS_SUCCESS

    def load_config(self, config_obj=None):
        """
            Load a configuration file
        """
        if config_obj is None:
            log.error("Missing configuration object!")
            sys.exit(1)

        try:
            self.config = ConfigObj(config_obj)
        except Exception, e:
            log.error("Error on reading configuration object {}! Error: {}".format(config_obj, e))
            sys.exit(1)

        return OS_SUCCESS

    def write_config(self):
        """
            Write the configuration to file
        """
        log.info("Writing configuration file {}".format(self.config_file))
        try:
            self.config.filename = self.config_file
            self.config.write()
        except Exception, e:
            log.error("Error when writing configuration file {}! Error: {}".format(self.config_file, e))
            sys.exit(1)

        return OS_SUCCESS

    def setup_config_dir(self):
        """
            Create the deployr configuration directory
        """
        fpath, fname = os.path.split(self.config_file)
        try:
            if not os.path.exists(fpath):
                os.mkdir(fpath)
        except Exception, e:
            log.error("Error when creating configuration directory {}".format(fpath))
            sys.exit(1)

        return OS_SUCCESS

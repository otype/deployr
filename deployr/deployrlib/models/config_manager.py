# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import os
import sys
from configobj import ConfigObj
from deployrlib.globals.return_codes import OS_SUCCESS
import logging

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

        logging.info("Setting configuration file {}".format(self.config_file))
        if not os.path.exists(self.config_file):
            logging.error("Cannot load configuration file {}: not found!".format(self.config_file))
            sys.exit(1)

        try:
            self.config = ConfigObj(self.config_file)
        except Exception, e:
            logging.error("Error on reading configuration file {}! Error: {}".format(self.config_file, e))
            sys.exit(1)

        return OS_SUCCESS

    def load_config(self, config_obj=None):
        """
            Load a configuration file
        """
        if config_obj is None:
            logging.error("Missing configuration object!")
            sys.exit(1)

        try:
            self.config = ConfigObj(config_obj)
        except Exception, e:
            logging.error("Error on reading configuration object {}! Error: {}".format(config_obj, e))
            sys.exit(1)

        return OS_SUCCESS

    def write_config(self):
        """
            Write the configuration to file
        """
        logging.info("Writing configuration file {}".format(self.config_file))
        try:
            self.config.filename = self.config_file
            self.config.write()
        except Exception, e:
            logging.error("Error when writing configuration file {}! Error: {}".format(self.config_file, e))
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
            logging.error("Error when creating configuration directory {}! Error: {}".format(fpath, e))
            sys.exit(1)

        return OS_SUCCESS

# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import os
from configobj import ConfigObj
from errors.exception_definitions import FileNotFoundException
from settings.config_settings import DEPLOYR_CONFIG_FILE


class ConfigManager(object):
    """
        The config manager for managing shared config values
    """

    def __init__(self, config_filename=DEPLOYR_CONFIG_FILE):
        """
            Initialize with the given config filename
        """
        self.config_filename = config_filename
        self.read()

    def read(self):
        """
            Read the configuration file
        """
        if os.path.exists(self.config_filename):
            self.config = ConfigObj(self.config_filename)
        else:
            self.config = None
            raise FileNotFoundException('File {} not found.'.format(self.config_filename))

    def update(self, modified_configs_hash):
        """
            Update a config with new values (all in a hash)
        """
        pass

    def write(self):
        """
            Write a config to file
        """
        self.config.write()

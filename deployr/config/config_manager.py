# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
#import os
#from configobj import ConfigObj
#from config.environment_configuration import ENVIRONMENT, GLOBAL_CONF
#from errors.exception_definitions import FileNotFoundException
#
#
#class ConfigManager(object):
#    """
#        The config manager for managing shared config values
#    """
#
#    def __init__(self, current_env=ENVIRONMENT.DEV):
#        """
#            Initialize with the given config filename
#        """
#        self.env = current_env
#        self.config = GLOBAL_CONF[current_env]
#        self.config_filename = self.config['DEPLOYR_CONFIG_FILE']
#        self.read()
#
#    def read(self):
#        """
#            Read the configuration file
#        """
#        if os.path.exists(self.config_filename):
#            self.config = ConfigObj(self.config_filename)
#        else:
#            self.config = None
#            raise FileNotFoundException('File {} not found.'.format(self.config_filename))
#
#    def update(self, modified_configs_hash):
#        """
#            Update a config with new values (all in a hash)
#        """
#        pass
#
#    def write(self):
#        """
#            Write a config to file
#        """
#        self.config.write()

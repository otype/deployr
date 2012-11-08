# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys
import os
import subprocess
from ostools import OS_SUCCESS, OS_ERROR
from config.logging_configuration import logger as log
from ostools.filewriter import write_genapi_backends_tpl
from ostools.filewriter import write_genapi_frontends_tpl

##############################################################################
#
# helper functions
#
##############################################################################

def base_config_path():
    """
        Construct the base path depending on the running platform we are on.
    """
    if sys.platform == 'darwin':
        return '.'
    elif sys.platform == 'linux2':
        return '/etc/haproxy'
    else:
        return '.'


def create_and_fetch_backends_directory(api_id):
    """
        Creates the necessary /etc/haproxy/backends/<api_id>-cluster directory
        for the backends config file.
    """
    backends_path = '{}/backends/{}-cluster'.format(base_config_path(), api_id)
    if not os.path.exists(backends_path):
        os.mkdir(backends_path, 0755)
    return backends_path


def get_backends_config_file(api_id):
    """
        Define the backends config file.
    """
    return '{}/100-{}'.format(create_and_fetch_backends_directory(api_id), api_id)


def get_frontends_config_file(api_id):
    """
        Define the frontends config file.
    """
    return '{}/frontends/http_proxy/100-{}'.format(base_config_path(), api_id)

def reload_haproxy():
    return subprocess.call['/etc/init.d/haproxy', 'reload']

##############################################################################
#
# main call methods
#
##############################################################################

def loadbalance_update_api(api_id, api_host, api_port):
    """
        Write the backends and frontends configuration file for haproxy
        for a given deployed API.
    """
    # get the config file names
    backends_config = get_backends_config_file(api_id=api_id)
    frontends_config = get_frontends_config_file(api_id=api_id)

    # Write the backends config
    log.info('Writing configuration {} for API: {}'.format(backends_config, api_id))
    write_genapi_backends_tpl(config_file_name=backends_config, api_id=api_id, api_host=api_host, api_port=api_port)

    # write the frontends config
    log.info('Writing configuration {} for API: {}'.format(frontends_config, api_id))
    write_genapi_frontends_tpl(config_file_name=frontends_config, api_id=api_id)

    # add the config (implicitly starts the genapi)
    log.info('Trying to reload loadbalancer (haproxy), now ...')

    status_code = OS_SUCCESS
    if not reload_haproxy():
        log.error("Error on reloading haproxy.")
        status_code = OS_ERROR

    return status_code

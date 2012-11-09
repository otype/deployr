# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import sys
from config.logging_configuration import logger as log
from config.genapi_template_settings import GENAPI_START_SCRIPT
from config.genapi_template_settings import GENAPI_PYTHON_EXEC
from config.genapi_template_settings import GENAPI_HOME_DIRECTORY
from config.genapi_template_settings import GENAPI_USER
from ostools import OS_SUCCESS, OS_ERROR
from ostools import get_local_public_ip_address
from ostools import get_open_port
from ostools.filewriter import write_genapi_base_tpl
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_reload_config
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_get_process_info
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_remove_group
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_stop
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_add_group

##############################################################################
#
# helper functions
#
##############################################################################


def define_config_file_name(api_id):
    """
        Define the config file name depending on the platform.
    """
    if sys.platform == 'darwin':
        config_file_name = '{}.conf'.format(api_id)
    elif sys.platform == 'linux2':
        config_file_name = '/etc/supervisor.d/{}.conf'.format(api_id)
    else:
        config_file_name = '{}.conf'.format(api_id)
    return config_file_name


def is_already_running(api_id):
    """
        Check if API with given API ID is running or not.
    """
    process_info = supervisor_xmlrpc_get_process_info(api_id)
    if process_info is None:
        return False

    if process_info == OS_ERROR:
        log.error('API is not running or connection to supervisor failed!')
        return False

    if process_info['statename'] != 'RUNNING':
        return False

    return True

##############################################################################
#
# main call methods
#
##############################################################################


def deploy_api(api_id, db_host, genapi_version, log_level, environment, entities):
    """
        Deploy an GenAPI
    """
    assigned_port = get_open_port()
    log.debug('Assigning port: {}'.format(assigned_port))

    application_host = get_local_public_ip_address()
    log.debug('Current host is {}'.format(application_host))

    config_file_name = define_config_file_name(api_id=api_id)
    log.debug('Configuration file name is {}'.format(config_file_name))

    # Write the supervisor config
    log.info('Writing configuration for API: {}'.format(api_id))
    write_genapi_base_tpl(
        genapi_api_id=api_id,
        python_interpreter=GENAPI_PYTHON_EXEC,
        genapi_start=GENAPI_START_SCRIPT,
        logging_level=log_level,
        riak_host=db_host,
        app_port=assigned_port,
        genapi_version=genapi_version,
        genapi_env=environment,
        genapi_entity_list=entities,
        genapi_home_directory=GENAPI_HOME_DIRECTORY,
        genapi_user=GENAPI_USER,
        genapi_log_file='{}/genapi_{}.log'.format(GENAPI_HOME_DIRECTORY, api_id),
        config_file_name=config_file_name
    )

    # If an API with given API ID is already running, we stop that one, first.
    if is_already_running(api_id=api_id):
        log.info('An API with API ID=\'{}\' is already running! Stopping it, first.'.format(api_id))
        supervisor_xmlrpc_stop(api_id)

        log.info('Removing API ID=\'{}\''.format(api_id))
        supervisor_xmlrpc_remove_group(api_id)

    # Re-read the configuration files
    supervisor_xmlrpc_reload_config()

    # add the config (implicitly starts the genapi)
    log.info('Adding (deploying) new API with API ID=\'{}\' on host=\'{}\' on port=\'{}\''.format(
        api_id, application_host, assigned_port)
    )
    supervisor_xmlrpc_add_group(api_id)

    return OS_SUCCESS, application_host, assigned_port

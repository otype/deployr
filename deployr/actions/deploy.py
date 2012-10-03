# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import sys
from ostools import OS_SUCCESS
from ostools.filewriter import write_supervisor_config_for_api
from ostools.path_finders import python_interpreter_path
from ostools.port_acquisition import get_open_port
from messagequeue.message_tx import send_message
from supervisor.supervisor_xml_rpc_api import supervisor_xmlrpc_reload_config
from supervisor.supervisor_xml_rpc_api import supervisor_xmlrpc_start
from task.messages.deploy_confirmation import DeployConfirmation

##############################################################################
#
# helper functions
#
##############################################################################


def send_deploy_confirmation(api_id, genapi_version, host, port, status):
    """
        Send confirmation message
    """
    deploy_confirmation_message = DeployConfirmation(
        api_id=api_id,
        genapi_version=genapi_version,
        host=host,
        port=port,
        status=status
    ).to_json()

    return send_message(deploy_confirmation_message)

##############################################################################
#
# main call methods
#
##############################################################################


def deploy_api(api_id, db_host, genapi_version, log_level, entities):
    """
        Deploy an GenAPI
    """
    assigned_port = get_open_port()
    this_host = 'some.awesome.host'

    if sys.platform == 'darwin':
        config_file_name = '/etc/supervisor/conf.d/{}.conf'.format(api_id)
    elif sys.platform == 'linux2':
        config_file_name = '{}.conf'.format(api_id)
    else:
        config_file_name = '{}.conf'.format(api_id)

    # Write the supervisor config
    write_supervisor_config_for_api(
        genapi_api_id=api_id,
        python_interpreter=python_interpreter_path(),
        genapi_start='/home/genapi/pygenapi/genapi/start.py',
        logging_level=log_level,
        riak_host=db_host,
        app_port=assigned_port,
        genapi_version=genapi_version,
        genapi_entity_list=entities,
        genapi_home_directory='/home/genapi',
        genapi_user='genapi',
        genapi_log_file='/home/genapi/log/genapi_{}.log'.format(api_id),
        config_file_name=config_file_name
    )

    # Re-read the configuration files
    supervisor_xmlrpc_reload_config()

    # now, start the application
    supervisor_xmlrpc_start(api_id)

    # Send out the confirmation message
    send_deploy_confirmation(
        api_id=api_id,
        genapi_version=genapi_version,
        host=this_host,
        port=assigned_port,
        status=1
    )

    return OS_SUCCESS

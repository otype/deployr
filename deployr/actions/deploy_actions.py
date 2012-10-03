# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from messagequeue.message_tx import send_message
from ostools import OS_SUCCESS
from ostools.filewriter import write_supervisor_config_for_api
from ostools.path_finders import python_interpreter_path
from ostools.port_acquisition import get_open_port
from supervisor.supervisor_xml_rpc_api import supervisor_xmlrpc_reread, supervisor_xmlrpc_start
from supervisor.supervisorctl_api import supervisorctl_reread
from supervisor.supervisorctl_api import supervisorctl_stop
from supervisor.supervisorctl_api import supervisorctl_remove
from task.deploy_confirmation_message import DeployConfirmationMessage


def send_deploy_confirmation(api_id, genapi_version, host, port, status):
    """
        Send confirmation message
    """
    deploy_confirmation_message = DeployConfirmationMessage(
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

    # Write the supervisor config
    write_supervisor_config_for_api(
        genapi_api_id=api_id,
        python_interpreter=python_interpreter_path(),
        genapi_start='/opt/genapis/genapi/start.py',
        logging_level=log_level,
        riak_host=db_host,
        app_port=assigned_port,
        genapi_version=genapi_version,
        genapi_entity_list=entities,
        genapi_home_directory='/opt/genapi',
        genapi_user='genapi',
        genapi_log_file='/opt/genapis/genapi_{}.log'.format(api_id),
        config_file_name='{}.conf'.format(api_id)
    )

    # Re-read the configuration files
    supervisor_xmlrpc_reread()

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


def undeploy_api(api_id):
    """
        Undeploy a currently deployed API with given API ID
    """
    # stop the API
    supervisorctl_stop(api_id)

    # remove all configuration from supervisorctl context
    supervisorctl_remove(api_id)

    # reread config files
    supervisorctl_reread()

    # delete configuration file from file system

    return OS_SUCCESS

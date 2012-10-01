# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import time
from jinja2.environment import Environment
from jinja2.loaders import PackageLoader
from messagequeue.message_tx import send_message
from ostools import OS_SUCCESS
from ostools.filewriter import write_supervisor_config_for_api
from ostools.path_finders import python_interpreter_path
from ostools.port_acquisition import get_open_port
from ostools.supervisorctl import supervisor_reread, supervisor_stop, supervisor_remove
from ostools.supervisorctl import supervisor_add
from ostools.supervisorctl import supervisor_start
from templates.template_definitions import DEPLOY_CONFIRMATION_TEMPLATE


def send_deploy_confirmation(self, api_id, genapi_version, host, port, status):
    """
        Send confirmation message
    """
    env = Environment(loader=PackageLoader('templates', 'message_queue_templates'))
    template = env.get_template(DEPLOY_CONFIRMATION_TEMPLATE)
    message = template.render(
        api_id=self.api_id,
        genapi_version=genapi_version,
        host=host,
        port=port,
        status=status,
        created_at=time.time()
    )
    send_message(message)


##############################################################################
#
# main call methods
#
##############################################################################


def deploy_api(api_id, db_host, genapi_version, log_level, entities):
    """
        Deploy an GenAPI
    """
    # Write the supervisor config
    write_supervisor_config_for_api(
        genapi_api_id=api_id,
        python_interpreter=python_interpreter_path(),
        genapi_start='/opt/genapis/genapi/start.py',
        logging_level=log_level,
        riak_host=db_host,
        app_port=get_open_port(),
        genapi_version=genapi_version,
        genapi_entity_list=entities,
        genapi_home_directory='/opt/genapi',
        genapi_user='genapi',
        genapi_log_file='/opt/genapis/genapi_{}.log'.format(api_id),
        config_file_name='{}.conf'.format(api_id)
    )

    # Re-read the configuration files
    supervisor_reread()

    # add the application to supervisor's context
    supervisor_add(api_id)

    # now, start the application
    supervisor_start(api_id)

    return OS_SUCCESS


def undeploy_api(api_id):
    """
        Undeploy a currently deployed API with given API ID
    """
    # stop the API
    supervisor_stop(api_id)

    # remove all configuration from supervisorctl context
    supervisor_remove(api_id)

    # reread config files
    supervisor_reread()

    # delete configuration file from file system

    return OS_SUCCESS

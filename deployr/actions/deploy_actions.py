# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from ostools.filewriter import write_supervisor_config_for_api
from ostools.path_finders import python_interpreter_path
from ostools.port_acquisition import get_open_port

##############################################################################
#
# helper functions and globals
#
##############################################################################


def reread_supervisor_configs():
    """
        Reread the supervisor configuration files
    """
    log.info('DUMMY: Reread the supervisor configurations files now.')


def start_genapi(genapi_api_id):
    """
        Start the GenAPI with given API ID
    """
    log.info('DUMMY: Start GenAPI with ID: {}'.format(genapi_api_id))

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
    reread_supervisor_configs()

    # Start the GenAPI
    start_genapi(api_id)

# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import os
from pika import log
import sys
from ostools import write_file
from constants.template_settings import GENAPI_CONFIG_TEMPLATE


##############################################################################
#
# helper functions
#
##############################################################################


def entity_list_as_csv(entity_list):
    """
        Create a comma-separated list of the entity array
    """
    return ','.join([str(i) for i in entity_list])


def get_template_base_dir():
    if sys.platform == 'darwin':
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))
    elif sys.platform == 'linux2':
        template_dir = "/etc/deployr/templates"
    else:
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))

    return template_dir


def genapi_template(python_interpreter, genapi_start, logging_level, riak_host, app_port, genapi_api_id,
                    genapi_version, genapi_entity_list, genapi_home_directory, genapi_user, genapi_log_file):

    env = Environment(loader=FileSystemLoader(get_template_base_dir()))
    template = env.get_template(GENAPI_CONFIG_TEMPLATE)
    log.debug("Template read: {}".format(template))

    return template.render(
        genapi_api_id=genapi_api_id,
        python_interpreter=python_interpreter,
        genapi_start=genapi_start,
        logging_level=logging_level,
        riak_host=riak_host,
        app_port=app_port,
        genapi_version=genapi_version,
        genapi_entity_list=entity_list_as_csv(genapi_entity_list),
        genapi_home_directory=genapi_home_directory,
        genapi_user=genapi_user,
        genapi_log_file=genapi_log_file
    )

##############################################################################
#
# main call methods
#
##############################################################################


def write_supervisor_config_for_api(python_interpreter, genapi_start, logging_level, riak_host, app_port,
                                    genapi_api_id, genapi_version, genapi_entity_list, genapi_home_directory,
                                    genapi_user, genapi_log_file, config_file_name):
    """
        Write a configuration file for a given API that will be readable by supervisord.
    """
    tpl = genapi_template(
        genapi_api_id=genapi_api_id,
        python_interpreter=python_interpreter,
        genapi_start=genapi_start,
        logging_level=logging_level,
        riak_host=riak_host,
        app_port=app_port,
        genapi_version=genapi_version,
        genapi_entity_list=genapi_entity_list,
        genapi_home_directory=genapi_home_directory,
        genapi_user=genapi_user,
        genapi_log_file=genapi_log_file
    )

    log.debug("Writing template: {}".format(tpl))
    write_file(filename=config_file_name, content=tpl)

    log.info('Supervisor configuration file written for API with id: {}'.format(genapi_api_id))

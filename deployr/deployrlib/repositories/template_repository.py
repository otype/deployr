# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 22:43 CET
    
    Copyright (c) 2012 apitrary

"""
import os
import sys
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader
from deployrlib.config.template_config import GENAPI_TEMPLATES_CONFIG
from deployrlib.services import filesystem_service, logging_service

#
# Logger
#
logger = logging_service.get_logger()

def entity_list_as_csv(entity_list):
    """
        Create a comma-separated list of the entity array
    """
    return ','.join([str(i) for i in entity_list])


def get_template_base_dir():
    """
        Depending on where deployr is run, we need to find the templates in
        a defined location.
    """
    if sys.platform == 'darwin':
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))
    elif sys.platform == 'linux2':
        template_dir = "/etc/deployr/templates"
    else:
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))

    return template_dir


def load_template(template_name):
    """
        Use jinja2 template engine to load the corresponding template file
    """
    env = Environment(loader=FileSystemLoader(get_template_base_dir()))
    template = env.get_template(template_name)
    logger.debug("Template read: {}".format(template))
    return template


def write_genapi_base_tpl(python_interpreter, genapi_start, logging_level, riak_host, app_port,
                          genapi_api_id, genapi_version, genapi_env, genapi_entity_list, genapi_api_key,
                          genapi_home_directory, genapi_user, genapi_log_file, config_file_name):
    """
        Write a configuration file for a given API that will be readable by supervisord.
    """
    # Load the template
    template = load_template(GENAPI_TEMPLATES_CONFIG['GENAPI_BASE']['GENAPI_BASE_TEMPLATE'])

    # Render the template with substituted values
    tpl = template.render(
        genapi_api_id=genapi_api_id,
        python_interpreter=python_interpreter,
        genapi_start=genapi_start,
        logging_level=logging_level,
        riak_host=riak_host,
        app_port=app_port,
        genapi_version=genapi_version,
        genapi_env=genapi_env,
        genapi_entity_list=entity_list_as_csv(genapi_entity_list),
        genapi_api_key=genapi_api_key,
        genapi_home_directory=genapi_home_directory,
        genapi_user=genapi_user,
        genapi_log_file=genapi_log_file
    )

    # And write the template.
    logger.debug("Writing template: {}".format(tpl))
    filesystem_service.write_file(filename=config_file_name, content=tpl)
    logger.info('Supervisor configuration file written for API with id: {}'.format(genapi_api_id))


def write_genapi_backends_tpl(config_file_name, api_id, api_host, api_port):
    """
        Write the haproxy backends part for an already deployed API in order
        to create the routing (part 1) on the loadbalancer.
    """
    # Load the template
    template = load_template(GENAPI_TEMPLATES_CONFIG['GENAPI_BACKENDS']['GENAPI_BACKENDS_TEMPLATE'])

    # Render the template with substituted values
    tpl = template.render(api_id=api_id, api_host=api_host, api_port=api_port)

    # And write the template.
    logger.debug("Writing template: {}".format(tpl))
    filesystem_service.write_file(filename=config_file_name, content=tpl)
    logger.info('Loadbalancer (haproxy) BACKENDS configuration written for API with id: {}'.format(api_id))


def write_genapi_frontends_tpl(config_file_name, api_id):
    """
        Write the haproxy backends part for an already deployed API in order
        to create the routing (part 1) on the loadbalancer.
    """
    # Load the template
    template = load_template(GENAPI_TEMPLATES_CONFIG['GENAPI_FRONTENDS']['GENAPI_FRONTENDS_TEMPLATE'])

    # Render the template with substituted values
    tpl = template.render(api_id=api_id)

    # And write the template.
    logger.debug("Writing template: {}".format(tpl))
    filesystem_service.write_file(filename=config_file_name, content=tpl)
    logger.info('Loadbalancer (haproxy) FRONTENDS configuration written for API with id: {}'.format(api_id))
# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 22:45 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import template_repository

def write_genapi_base_tpl(python_interpreter, genapi_start, logging_level, riak_host, app_port,
                          genapi_api_id, genapi_version, genapi_env, genapi_entity_list, genapi_api_key,
                          genapi_home_directory, genapi_user, genapi_log_file, config_file_name):
    """
        Write a configuration file for a given API that will be readable by supervisord.
    """
    return template_repository.write_genapi_base_tpl(
        python_interpreter=python_interpreter,
        genapi_start=genapi_start,
        logging_level=logging_level,
        riak_host=riak_host,
        app_port=app_port,
        genapi_api_id=genapi_api_id,
        genapi_version=genapi_version,
        genapi_env=genapi_env,
        genapi_entity_list=genapi_entity_list,
        genapi_api_key=genapi_api_key,
        genapi_home_directory=genapi_home_directory,
        genapi_user=genapi_user,
        genapi_log_file=genapi_log_file,
        config_file_name=config_file_name
    )


def write_genapi_backends_tpl(config_file_name, api_id, api_host, api_port):
    """
        Write the haproxy backends part for an already deployed API in order
        to create the routing (part 1) on the loadbalancer.
    """
    return template_repository.write_genapi_backends_tpl(
        config_file_name=config_file_name,
        api_id=api_id,
        api_host=api_host,
        api_port=api_port
    )


def write_genapi_frontends_tpl(config_file_name, api_id):
    """
        Write the haproxy backends part for an already deployed API in order
        to create the routing (part 1) on the loadbalancer.
    """
    return template_repository.write_genapi_frontends_tpl(
        config_file_name=config_file_name,
        api_id=api_id
    )
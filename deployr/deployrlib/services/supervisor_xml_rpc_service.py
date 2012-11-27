# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 27.11.12, 00:09 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import supervisor_xml_rpc_repository

def reload_config():
    """
        Reread the supervisor_api configuration files
    """
    return supervisor_xml_rpc_repository.reload_config()


def start(app_name):
    """
        Start given application via supervisor_api
    """
    return supervisor_xml_rpc_repository.start(app_name=app_name)


def stop(app_name):
    """
        Stop given application via supervisor_api
    """
    return supervisor_xml_rpc_repository.stop(app_name=app_name)


def restart(app_name):
    """
        Start given application via supervisor_api
    """
    return supervisor_xml_rpc_repository.restart(app_name=app_name)


def add_group(group_name):
    """
        Add new application to supervisor_api configuration
    """
    return supervisor_xml_rpc_repository.add_group(group_name=group_name)


def status():
    """
        Request status of given application
    """
    return supervisor_xml_rpc_repository.status()


def get_all_process_info():
    """
        Request status of given application
    """
    return supervisor_xml_rpc_repository.get_all_process_info()


def get_process_info(app_name):
    """
        Request status of given application
    """
    return supervisor_xml_rpc_repository.get_process_info(app_name=app_name)


def remove_group(group_name):
    """
        Remove application from supervisor_api context
    """
    return supervisor_xml_rpc_repository.remove_group(group_name=group_name)


def get_all_config_info():
    """
        Remove application from supervisor_api context
    """
    return supervisor_xml_rpc_repository.get_all_config_info()


def get_config_info(app_name):
    """
        Remove application from supervisor_api context
    """
    return supervisor_xml_rpc_repository.get_config_info(app_name=app_name)


def help_method(method_name):
    """
        Simple helper method to show the method's parameters and response values.
        Used purely for Development!
    """
    return supervisor_xml_rpc_repository.help_method(method_name=method_name)


def list_methods():
    """
        List all methods
    """
    return supervisor_xml_rpc_repository.list_methods()
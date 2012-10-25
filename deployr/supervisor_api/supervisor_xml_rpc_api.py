# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import xmlrpclib
from pika import log
from config.environment import CURRENT_CONFIGURATION
from ostools import OS_SUCCESS
from ostools import OS_ERROR


##############################################################################
#
# CONSTANTS
#
##############################################################################

# Contact XML-RPC on given address
SUPERVISOR_XML_RPC_SERVER_ADDRESS = CURRENT_CONFIGURATION['SUPERVISOR_XML_RPC_SERVER_ADDRESS']

# Supervisor server object
SUPERVISOR_XML_RPC_SERVER = xmlrpclib.Server(SUPERVISOR_XML_RPC_SERVER_ADDRESS)

##############################################################################
#
# API CALLS
#
##############################################################################


def supervisor_xmlrpc_reload_config():
    """
        Reread the supervisor_api configuration files
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting reload of all configs'.format(SUPERVISOR_XML_RPC_SERVER_ADDRESS))
    try:
        SUPERVISOR_XML_RPC_SERVER.supervisor.reloadConfig()
    except xmlrpclib.Fault, e:
        log.error('Could not reload config! Error: {}'.format(e))
        return OS_ERROR
    return OS_SUCCESS


def supervisor_xmlrpc_start(app_name):
    """
        Start given application via supervisor_api
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting start of application: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, app_name)
    )
    try:
        if SUPERVISOR_XML_RPC_SERVER.supervisor.startProcess(app_name):
            return OS_SUCCESS
    except xmlrpclib.Fault, e:
        log.error('Could not start process \'{}\'! Error: {}'.format(app_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_stop(app_name):
    """
        Stop given application via supervisor_api
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting stop of application: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, app_name)
    )
    try:
        if SUPERVISOR_XML_RPC_SERVER.supervisor.stopProcess(app_name):
            return OS_SUCCESS
    except xmlrpclib.Fault, e:
        log.error('Could not stop process \'{}\'! Error: {}'.format(app_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_restart(app_name):
    """
        Start given application via supervisor_api
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting restart of application: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, app_name)
    )

    stop_state = supervisor_xmlrpc_stop(app_name)
    start_state = supervisor_xmlrpc_start(app_name)

    if (stop_state + start_state) > OS_SUCCESS:
        log.error('Could not restart process \'{}\'!'.format(app_name))
        return OS_ERROR

    return OS_SUCCESS


def supervisor_xmlrpc_add_group(group_name):
    """
        Add new application to supervisor_api configuration
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting addition of application: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, group_name)
    )
    try:
        if SUPERVISOR_XML_RPC_SERVER.supervisor.addProcessGroup(group_name):
            return OS_SUCCESS
    except xmlrpclib.Fault, e:
        log.error('Could not add process group \'{}\'! Error: {}'.format(group_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_status():
    """
        Request status of given application
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting status'.format(SUPERVISOR_XML_RPC_SERVER_ADDRESS))
    try:
        response = SUPERVISOR_XML_RPC_SERVER.supervisor.getState()
        if 'statename' in response:
            if response['statename'] == 'RUNNING':
                log.debug('SUPERVISOR XML-RPC({}): Status \'{}\''.format(response['statename']))
                return OS_SUCCESS
        return OS_ERROR
    except xmlrpclib.Fault, e:
        log.error('Could not get status! Error: {}'.format(e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_get_all_process_info():
    """
        Request status of given application
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting all process info'.format(SUPERVISOR_XML_RPC_SERVER_ADDRESS))
    try:
        return SUPERVISOR_XML_RPC_SERVER.supervisor.getAllProcessInfo()
    except xmlrpclib.Fault, e:
        log.error('Could not get all process info! Error: {}'.format(e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_get_process_info(app_name):
    """
        Request status of given application
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting process info for api_id: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, app_name)
    )
    try:
        all_processes = SUPERVISOR_XML_RPC_SERVER.supervisor.getAllProcessInfo()
        for process in all_processes:
            if 'name' in process:
                if process['name'] == app_name:
                    return process
        return None
    except xmlrpclib.Fault, e:
        log.error('Could not get the process info for: {}! Error: {}'.format(app_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_remove_group(group_name):
    """
        Remove application from supervisor_api context
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting removal of group: {}'.format(
        SUPERVISOR_XML_RPC_SERVER_ADDRESS, group_name)
    )
    try:
        if SUPERVISOR_XML_RPC_SERVER.supervisor.removeProcessGroup(group_name):
            return OS_SUCCESS
    except xmlrpclib.Fault, e:
        log.error('Could not remove process group \'{}\'! Error: {}'.format(group_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_get_all_config_info():
    """
        Remove application from supervisor_api context
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting all config info'.format(SUPERVISOR_XML_RPC_SERVER_ADDRESS))
    try:
        return SUPERVISOR_XML_RPC_SERVER.supervisor.getAllConfigInfo()
    except xmlrpclib.Fault, e:
        log.error('Could not get all config info! Error: {}'.format(e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_get_config_info(app_name):
    """
        Remove application from supervisor_api context
    """
    log.debug('SUPERVISOR XML-RPC({}): Requesting all config info'.format(SUPERVISOR_XML_RPC_SERVER_ADDRESS))
    try:
        all_configs = SUPERVISOR_XML_RPC_SERVER.supervisor.getAllConfigInfo()
        for config in all_configs:
            if 'group' in config:
                if config['group'] == app_name:
                    return config
        return None
    except xmlrpclib.Fault, e:
        log.error('Could not get config info for API: {}! Error: {}'.format(app_name, e))
        return OS_ERROR
    except Exception, e:
        log.error('Unknown error! Call the administrator! Error: {}'.format(e))
        return OS_ERROR


def supervisor_xmlrpc_help_method(method_name):
    """
        Simple helper method to show the method's parameters and response values.
        Used purely for Development!
    """
    try:
        print SUPERVISOR_XML_RPC_SERVER.system.methodHelp(method_name)
    except xmlrpclib.Fault, e:
        log.warning('Received no result on given method! Error: {}'.format(e))
        return OS_ERROR
    return OS_SUCCESS


def supervisor_xmlrpc_list_methods():
    """
        List all methods
    """
    try:
        print SUPERVISOR_XML_RPC_SERVER.system.listMethods()
    except xmlrpclib.Fault, e:
        log.warning('Received no result on given method! Error: {}'.format(e))
        return OS_ERROR
    return OS_SUCCESS
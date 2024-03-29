# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from deployrlib.globals.return_codes import OS_SUCCESS
from deployrlib.services import supervisorctl_service


def undeploy_api(api_id):
    """
        Undeploy a currently deployed API with given API ID
    """
    # stop the API
    supervisorctl_service.supervisorctl_stop(api_id)

    # remove all configuration from supervisorctl context
    supervisorctl_service.supervisorctl_remove(api_id)

    # reread config files
    supervisorctl_service.supervisorctl_reread()

    # delete configuration file from file system
    return OS_SUCCESS

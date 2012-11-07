# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from ostools import OS_SUCCESS
from supervisor_api.supervisorctl_api import supervisorctl_stop
from supervisor_api.supervisorctl_api import supervisorctl_remove
from supervisor_api.supervisorctl_api import supervisorctl_reread

##############################################################################
#
# main call methods
#
##############################################################################


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

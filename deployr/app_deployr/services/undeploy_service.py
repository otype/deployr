# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 27.11.12, 00:40 CET
    
    Copyright (c) 2012 apitrary

"""
from app_deployr.repositories import undeploy_repository

def undeploy_api(api_id):
    """
        Undeploy a currently deployed API with given API ID
    """
    return undeploy_repository.undeploy_api(api_id=api_id)
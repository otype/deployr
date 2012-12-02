# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 23:45 CET
    
    Copyright (c) 2012 apitrary

"""
from app_deployr.repositories import deploy_repository

def deploy_api(api_id, db_host, genapi_version, log_level, environment, entities, api_key):
    """
        Deploy an GenAPI
    """
    return deploy_repository.deploy_api(
        api_id=api_id,
        db_host=db_host,
        genapi_version=genapi_version,
        log_level=log_level,
        environment=environment,
        entities=entities,
        api_key=api_key
    )
# -*- coding: utf-8 -*-
"""

    <application_name>    

    created by hgschmidt on 27.11.12, 00:34 CET
    
    Copyright (c) 2012 apitrary

"""
from lb_deployr.repositories import haproxy_repository

def reload_haproxy():
    """
        Reload the haproxy server
    """
    return haproxy_repository.reload_haproxy()
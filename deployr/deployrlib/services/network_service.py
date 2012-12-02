# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 26.11.12, 22:36 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.repositories import network_repository

def get_host_name():
    """
        Get the hostname
    """
    return network_repository.get_host_name()


def get_open_port():
    """
        Responsible for getting a free port.
    """
    return network_repository.get_open_port()


def get_local_public_ip_address():
    """
        Get the public IP address for this host
    """
    return network_repository.get_local_public_ip_address()
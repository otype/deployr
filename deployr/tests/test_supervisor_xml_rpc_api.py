# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from ostools import OS_SUCCESS
from supervisor_api.supervisor_xml_rpc_api import supervisor_xmlrpc_reload_config


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


def test_supervisor_xmlrpc_reload_config():
    """
        Works if the correct host settings and credentials are set in
        the current configuration hash.
    """
    assert OS_SUCCESS == supervisor_xmlrpc_reload_config()

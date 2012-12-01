# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from deployrlib.globals.return_codes import OS_SUCCESS
from deployrlib.services.supervisor_xml_rpc_service import reload_config


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


def test_supervisor_xmlrpc_reload_config():
    """
        Works if the correct host settings and credentials are set in
        the current configuration hash.
    """
    assert OS_SUCCESS == reload_config()

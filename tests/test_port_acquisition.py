# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from deployrlib.services.network_service import get_open_port


def setup_func():
    pass


def teardown_func():
    pass


def test_get_open_port():
    assert int == type(get_open_port())

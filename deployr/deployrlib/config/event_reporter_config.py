# -*- coding: utf-8 -*-
"""

    deployr

    created by hgschmidt on 02.12.12, 20:37 CET
    
    Copyright (c) 2012 apitrary

"""
from deployrlib.models.environments import ENVIRONMENT

EVENT_REPORTER_CONFIG = {

    ENVIRONMENT.TEST: {
        # Event Reporter API URL
        'API_URL': '127.0.0.1',

        # API Key
        'API_KEY': 'abcabcabcabc'
    },
    ENVIRONMENT.DEV: {
        # Event Reporter API URL
        'EVENT_REPORTER_URL': 'http://cdf90a6f3cb944f29ac5b26172f9761f.dev.api.apitrary.com',

        # API Key
        'API_KEY': 'abcabcabcabc'
    },
    ENVIRONMENT.LIVE: {
        # Event Reporter API URL
        'EVENT_REPORTER_URL': 'http://TO_BE_DEFINED.api.apitrary.com',

        # API Key
        'API_KEY': 'abcabcabcabc'
    }
}
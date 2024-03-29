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
        'API_KEY': '8458dc85b6ab1f66b49d2abf9b2b3c269ac478f14ad45ee3f39074b0822158ab'
    },
    ENVIRONMENT.LIVE: {
        # Event Reporter API URL
        'EVENT_REPORTER_URL': 'http://998099c5a38944f1a381d079bf7d5251.api.apitrary.com',

        # API Key
        'API_KEY': '22d3b69b893cdceb81806747ffcfd7ccc776ddae4a099e1116b9d64ee796f6e4'
    }
}
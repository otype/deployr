# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""


class ENVIRONMENT:
    """
        Self-defined enumeration
    """
    # for Test environment
    TEST = 'test'

    # for Dev environment
    DEV = 'dev'

    # for Live environment
    LIVE = 'live'


class LOGGING_LEVEL:
    """
        Accepted log levels for pika.log
    """
    DEBUG = 'debug'
    INFO = 'info'
    WARN = 'warning'


# GLOBAL CONFIGURATION HASH
#
#
GLOBAL_CONF = {

    # TEST ENVIRONMENT
    #
    #
    ENVIRONMENT.TEST: {
        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': 'deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': '127.0.0.1',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Contact XML-RPC on given address
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://127.0.0.1:9001/RPC2',

        # Message Queue Broker host
        'BROKER_HOST': '127.0.0.1',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Default log level
        'LOGGING': LOGGING_LEVEL.DEBUG

    },

    # DEV ENVIRONMENT
    #
    #
    ENVIRONMENT.DEV: {
        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': 'deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': '127.0.0.1',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Contact XML-RPC on given address
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://127.0.0.1:9001/RPC2',

        # Message Queue Broker host
        'BROKER_HOST': '127.0.0.1',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Default log level
        'LOGGING': LOGGING_LEVEL.DEBUG
    },

    # LIVE ENVIRONMENT
    #
    #
    ENVIRONMENT.LIVE: {
        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': '/etc/deployr/deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': '127.0.0.1',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Contact XML-RPC on given address
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://127.0.0.1:9001/RPC2',

        # Message Queue Broker host
        'BROKER_HOST': '127.0.0.1',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Default log level
        'LOGGING': LOGGING_LEVEL.INFO
    }
}

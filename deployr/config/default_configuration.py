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
        # Name of this environment
        'NAME': ENVIRONMENT.TEST,

        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': 'deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': '127.0.0.1',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Supervisor XML-RPC Credentials
        'SUPERVISOR_XML_RPC_USERNAME': 'UNSET',
        'SUPERVISOR_XML_RPC_PASSWORD': 'UNSET',

        # Contact XML-RPC on given address
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://127.0.0.1:9001/RPC2',

        # Message Queue Broker host
        'BROKER_HOST': '127.0.0.1',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Only accepting one message at a time ...
        'BROKER_PREFETCH_COUNT': False,

        # Message Queue User
        'BROKER_USER': 'UNSET',

        # Message Queue User
        'BROKER_PASSWORD': 'UNSET',

        # Default log level
        'LOGGING': LOGGING_LEVEL.DEBUG
    },

    # DEV ENVIRONMENT
    #
    #
    ENVIRONMENT.DEV: {
        # Name of this environment
        'NAME': ENVIRONMENT.DEV,

        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': 'deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': 'app1.dev.apitrary.net',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Supervisor XML-RPC Credentials
        'SUPERVISOR_XML_RPC_USERNAME': 'UNSET',
        'SUPERVISOR_XML_RPC_PASSWORD': 'UNSET',

        # Contact XML-RPC on given address with given credentials
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://{}:{}@app1.dev.apitrary.net:9001/RPC2'.format(
            'UNSET',      # USER NAME (see Chef recipe "supervisor" and role "pythonenv")
            'UNSET'       # PASSWORD  (see Chef recipe "supervisor" and role "pythonenv")
        ),

        # Message Queue Broker host
        'BROKER_HOST': 'rmq1.dev.apitrary.net',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Only accepting one message at a time ...
        'BROKER_PREFETCH_COUNT': False,

        # Message Queue User
        'BROKER_USER': 'UNSET',

        # Message Queue User
        'BROKER_PASSWORD': 'UNSET',

        # Default log level
        'LOGGING': LOGGING_LEVEL.DEBUG
    },

    # LIVE ENVIRONMENT
    #
    #
    ENVIRONMENT.LIVE: {
        # Name of this environment
        'NAME': ENVIRONMENT.LIVE,

        # Configuration file for deployr
        'DEPLOYR_CONFIG_FILE': '/etc/deployr/deployr.conf',

        # SUPERVISORD HOST
        'SUPERVISORD_HOST': '127.0.0.1',

        # SUPERVISORD WEB PORT
        #
        # XML-RPC web API of a running supervisord.
        # NEEDS TO BE ACTIVATED IN THE CONFIGS!
        'SUPERVISORD_WEB_PORT': 9001,

        # Supervisor XML-RPC Credentials
        'SUPERVISOR_XML_RPC_USERNAME': 'UNSET',
        'SUPERVISOR_XML_RPC_PASSWORD': 'UNSET',

        # Contact XML-RPC on given address with given credentials
        'SUPERVISOR_XML_RPC_SERVER_ADDRESS': 'http://{}:{}@127.0.0.1:9001/RPC2'.format(
            'UNSET',     # USER NAME (see Chef recipe "supervisor" and role "pythonenv")
            'UNSET'      # PASSWORD  (see Chef recipe "supervisor" and role "pythonenv")
        ),

        # Message Queue Broker host
        'BROKER_HOST': 'rmq1.live.apitrary.net',

        # Message Queue Broker port
        'BROKER_PORT': 5672,

        # Only accepting one message at a time ...
        'BROKER_PREFETCH_COUNT': False,

        # Message Queue User
        'BROKER_USER': 'UNSET',

        # Message Queue User
        'BROKER_PASSWORD': 'UNSET',

        # Default log level
        'LOGGING': LOGGING_LEVEL.INFO
    }
}

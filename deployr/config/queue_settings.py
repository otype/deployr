# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""

# BROKER HOST
#
# Where to find the broker.
#BROKER_HOST = '127.0.0.1'
BROKER_HOST = 'rmq1.apitrary.net'

# BROKER PORT
#
# On which port the broker is listening.
BROKER_PORT = 5672

# Message Queue name
#
#
GENAPI_DEPLOYMENT_QUEUE = 'genapi_deployment_queue'
GENAPI_DEPLOYMENT_CONFIRMATION_QUEUE = 'genapi_deployment_confirmation_queue'


# Routing keys
#
#
DEPLOY_ROUTING_KEY = GENAPI_DEPLOYMENT_QUEUE
DEPLOY_CONFIRMATION_ROUTING_KEY = GENAPI_DEPLOYMENT_CONFIRMATION_QUEUE
UNDEPLOY_ROUTING_KEY = GENAPI_DEPLOYMENT_QUEUE
UNDEPLOY_CONFIRMATION_ROUTING_KEY = GENAPI_DEPLOYMENT_CONFIRMATION_QUEUE

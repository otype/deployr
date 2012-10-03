# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""

# BROKER HOST
#
# Where to find the broker.
BROKER_HOST = '127.0.0.1'

# BROKER PORT
#
# On which port the broker is listening.
BROKER_PORT = 5672

# Exchange name
#
#
GENAPI_DEPLOYMENT_EXCHANGE = 'genapi_deployment_exchange'


# Message Queue name
#
#
GENAPI_DEPLOYMENT_QUEUE = 'genapi_deployment_exchange_queue'


# Routing keys
#
#
DEPLOY_ROUTING_KEY = 'apitrary.genapi.deploy.request'
DEPLOY_CONFIRMATION_ROUTING_KEY = 'apitrary.genapi.deploy.confirmation'
UNDEPLOY_ROUTING_KEY = 'apitrary.genapi.undeploy.request'
UNDEPLOY_CONFIRMATION_ROUTING_KEY = 'apitrary.genapi.undeploy.confirmation'

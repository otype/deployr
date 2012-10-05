# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import json
import time
from config.queue_settings import DEPLOY_CONFIRMATION_ROUTING_KEY
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE


class DeployConfirmationMessage(object):
    """
        A message object that is used for confirming a successful deployment
    """

    # the routing key for deploy confirmation
    routing_key = DEPLOY_CONFIRMATION_ROUTING_KEY

    # the exchange to use
    exchange = GENAPI_DEPLOYMENT_EXCHANGE

    def __init__(self, api_id, genapi_version, host, port, status):
        """
            Setting the base variables for this message object
        """
        self.api_id = api_id
        self.genapi_version = genapi_version
        self.host = host
        self.port = port
        self.status = status
        self.created_at = time.time()

    def to_dict(self):
        """
            Return a dictionary (JSON) from this object
        """
        return {
            'task_type': 'DEPLOY_CONFIRMATION',
            'api_id': self.api_id,
            'genapi_version': self.genapi_version,
            'host': self.host,
            'port': self.port,
            'status': self.status,
            'created_at': self.created_at
        }

    def to_json(self):
        """
            Return a JSON object
        """
        return json.dumps(self.to_dict())

# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import json
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE
from config.queue_settings import UNDEPLOY_CONFIRMATION_ROUTING_KEY


class UndeployConfirmationMessage(object):
    """
        An undeploy message
    """

    # the routing key for deploy confirmation
    routing_key = UNDEPLOY_CONFIRMATION_ROUTING_KEY

    # the exchange to use
    exchange = GENAPI_DEPLOYMENT_EXCHANGE

    def __init__(self, api_id, status):
        """
            Setting the base variables for this message object
        """
        self.api_id = api_id
        self.status = status

    def to_dict(self):
        """
            Return a dictionary (JSON) from this object
        """
        return {
            'task_type': 'UNDEPLOY_CONFIRMATION',
            'api_id': self.api_id,
            'status': self.status
        }

    def to_json(self):
        """
            Return a JSON object
        """
        return json.dumps(self.to_dict())

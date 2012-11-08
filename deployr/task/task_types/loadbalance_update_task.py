# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from messagequeue.blocking_message_tx import BlockingMessageTx
from task.actions.loadbalance_update import loadbalance_update_api
from task.messages.loadbalance_update_confirmation_message import LoadbalanceUpdateConfirmationMessage
from task.task_types.base_task import BaseTask


class LoadbalanceUpdateTask(BaseTask):
    """
        Undeploy task definition
    """

    def __init__(self, message, config):
        """
            Initialize the Deploy task
        """
        attribute_list = ['task_type', 'api_id', 'api_host', 'api_port']
        super(LoadbalanceUpdateTask, self).__init__(message, attribute_list, config)

    def parse_parameters(self):
        """
            Read out all parameters needed to run the deploy task
        """
        self.task_type = self.get_task_type()
        self.api_id = self.message['api_id']
        self.api_host = self.message['api_host']
        self.api_port = self.message['api_port']

    def run(self):
        """
            Hooked-up method to run when undeploying an API
        """
        self.last_execution_status = loadbalance_update_api(
            api_id=self.api_id,
            api_host=self.api_host,
            api_port=self.api_port
        )

        return self.last_execution_status

    def send_confirmation(self):
        """
            Send confirmation message
        """
        loadbalance_update_confirmation_message = LoadbalanceUpdateConfirmationMessage(
            api_id=self.api_id,
            lb_host='api.apitrary.com',
            lb_api_port=80,
            api_domainname='{}.api.apitrary.com'.format(self.api_id)
        )

        message_tx = BlockingMessageTx(self.config)
        return message_tx.send(message=loadbalance_update_confirmation_message)

# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from config.environment import CURRENT_CONFIGURATION
from messagequeue.blocking_message_tx import BlockingMessageTx
from ostools import OS_SUCCESS
from task.messages.loadbalance_update_confirmation_message import LoadbalanceUpdateConfirmationMessage
from task.task_types.base_task import BaseTask


class LoadbalanceUpdateTask(BaseTask):
    """
        Undeploy task definition
    """

    def __init__(self, message):
        """
            Initialize the Deploy task
        """
        attribute_list = ['task_type', 'api_id', 'api_host', 'api_port']
        super(LoadbalanceUpdateTask, self).__init__(message, attribute_list)

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
        # TODO: This is fake!
        self.last_execution_status = OS_SUCCESS
        return self.last_execution_status

    def send_confirmation(self, broker_host=CURRENT_CONFIGURATION['BROKER_HOST']):
        """
            Send confirmation message
        """
        loadbalance_update_confirmation_message = LoadbalanceUpdateConfirmationMessage(
            api_id=self.api_id,
            lb_host='fake.apitrary.com',
            lb_api_port=9999,
            api_domainname='fake.domain.apitrary.com'
        )

        message_tx = BlockingMessageTx(broker_host=broker_host)
        return message_tx.send(message=loadbalance_update_confirmation_message)
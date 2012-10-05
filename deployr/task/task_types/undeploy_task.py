# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from actions.undeploy import undeploy_api
from settings.queue_settings import BROKER_HOST
from messagequeue.blocking_message_tx import BlockingMessageTx
from task.messages.undeploy_confirmation_message import UndeployConfirmationMessage
from task.task_types.base_task import BaseTask


class UndeployTask(BaseTask):
    """
        Undeploy task definition
    """

    def __init__(self, message):
        """
            Initialize the Deploy task
        """
        attribute_list = ['task_type', 'api_id']
        super(UndeployTask, self).__init__(message, attribute_list)

    def parse_parameters(self):
        """
            Read out all parameters needed to run the deploy task
        """
        self.task_type = self.get_task_type()
        self.api_id = self.message['api_id']

    def run(self):
        """
            Hooked-up method to run when undeploying an API
        """
        self.last_execution_status = undeploy_api(api_id=self.api_id)
        return self.last_execution_status

    def send_confirmation(self, broker_host=BROKER_HOST):
        """
            Send confirmation message
        """
        undeploy_confirmation_message = UndeployConfirmationMessage(
            api_id=self.api_id,
            status=self.last_execution_status
        )

        message_tx = BlockingMessageTx(broker_host=broker_host)
        return message_tx.send(message=undeploy_confirmation_message)

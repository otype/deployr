# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from pika import log
from actions.deploy import deploy_api
from config.queue_settings import BROKER_HOST
from messagequeue.blocking_message_tx import BlockingMessageTx
from ostools import OS_ERROR
from task.messages.deploy_confirmation_message import DeployConfirmationMessage
from task.task_types.base_task import BaseTask


class DeployTask(BaseTask):
    """
        Deploy task definition
    """

    def __init__(self, message):
        """
            Initialize the Deploy task
        """
        attribute_list = ['task_type', 'api_id', 'db_host', 'db_port', 'genapi_version', 'log_level',
                          'entities', 'api_key']
        super(DeployTask, self).__init__(message, attribute_list)

    def parse_parameters(self):
        """
            Read out all parameters needed to run the deploy task

            {
                “task_type”: ”DEPLOY”,
                “api_id”: “88sdhv98shdvlh123”,
                “db_host”: “db1.apitrary.net”,
                “db_port”: 8098,
                “genapi_version”: 1,
                “log_level”: “debug”,
                “entities”: [ “user”, “object”, “contact” ],
                “api_key”: “iis9nd9vnsdvoijsdvoin9s8dv”
            }

        """
        self.task_type = self.get_task_type()
        self.api_id = self.message['api_id']
        self.db_host = self.message['db_host']
        self.genapi_version = self.message['genapi_version']
        self.log_level = self.message['log_level']
        self.entities = self.message['entities']

    def run(self):
        """
            Hooked-up method to run when deploying an API
        """
        status_code, application_host, assigned_port = deploy_api(
            api_id=self.api_id,
            db_host=self.db_host,
            genapi_version=self.genapi_version,
            log_level=self.log_level,
            entities=self.entities
        )

        self.last_execution_status = status_code
        self.application_host = application_host
        self.assigned_port = assigned_port

        return self.last_execution_status

    def send_confirmation(self, broker_host=BROKER_HOST):
        """
            Send confirmation message
        """
        if self.last_execution_status == OS_ERROR:
            log.error('Cannot send confirmation. Last run had an error.')
            return OS_ERROR

        deploy_confirmation_message = DeployConfirmationMessage(
            api_id=self.api_id,
            genapi_version=self.genapi_version,
            host=self.application_host,
            port=self.assigned_port,
            status=self.last_execution_status
        )

        message_tx = BlockingMessageTx(broker_host=broker_host)
        return message_tx.send(message=deploy_confirmation_message)
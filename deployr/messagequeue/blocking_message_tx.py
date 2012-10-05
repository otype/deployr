# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import json
import pika
from pika import log
from pika.adapters.blocking_connection import BlockingConnection
from config.queue_settings import BROKER_HOST
from config.queue_settings import BROKER_PORT
from errors.exception_definitions import UnacceptableMessageException
from ostools import OS_SUCCESS, OS_ERROR
from task.messages.deploy_confirmation_message import DeployConfirmationMessage
from task.messages.deploy_message import DeployMessage
from task.messages.undeploy_confirmation_message import UndeployConfirmationMessage
from task.messages.undeploy_message import UndeployMessage


class BlockingMessageTx(object):
    """
        Creates a blocking message transmission object. Provide the necessary
        broker connection parameters and a message, then send a message.
    """

    # Defines the topic exchange
    topic_type = 'topic'

    # content type of each message
    default_content_type = 'application/json'

    # set broker parameter durable
    durable = True

    # set broker parameter auto_delete
    auto_delete = False

    # all messages should be persisted in the queue (= 2)
    default_delivery_mode = 2

    # list of accepted message types
    accepted_message_types = [
        DeployMessage,
        DeployConfirmationMessage,
        UndeployMessage,
        UndeployConfirmationMessage
    ]

    def __init__(self, broker_host=BROKER_HOST, broker_port=BROKER_PORT):
        """
            Initialize for message and broker parameters
        """
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.parameters = pika.ConnectionParameters(host=broker_host, port=broker_port)
        log.debug('Broker host = \'{}\', Broker port = {}'.format(self.broker_host, self.broker_port))

    def is_valid_message(self):
        """
            Check if our message is one of our accepted types
        """
        if type(self.message) not in self.accepted_message_types:
            return False
        return True

    def setup(self):
        """
            Establish connection to broker.
        """
        self.connection = BlockingConnection(self.parameters)
        self.channel = self.connection.channel()
        log.debug('Connection established to broker: {}'.format(self.broker_host))

    def setup_exchange(self, exchange=None):
        """
            Declaring exchange for sending the deployment confirmation messages
        """
        if exchange:
            self.exchange = exchange

        log.debug('Declaring exchange=\'{}\', topic type=\'{}\''.format(self.exchange, self.topic_type))
        self.channel.exchange_declare(
            exchange=self.exchange,
            type=self.topic_type,
            durable=self.durable,
            auto_delete=self.auto_delete
        )

    def encoded_message(self):
        """
            Encode the message into the right format before sending.
        """
        log.debug('Encoding message: {}'.format(self.message.to_dict()))
        return json.dumps(self.message.to_dict())

    def publish(self, routing_key):
        """
            Publish the message to the queue
        """
        # set the routing key
        self.routing_key = routing_key

        # do we have a message?
        if not self.message:
            log.error('Missing message to publish!')
            return OS_ERROR

        # encode the message into correct format
        msg = self.encoded_message()

        log.info("Sending message: {}".format(msg))
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=msg,
            properties=pika.BasicProperties(
                content_type=self.default_content_type,
                delivery_mode=self.default_delivery_mode
            )
        )
        return OS_SUCCESS

    def tear_down(self):
        """
            Close the connection to the broker.
        """
        self.connection.close()
        log.debug('Connection to broker: {} closed'.format(self.broker_host))

    def send(self, message):
        """
            Send the message
        """
        # set the message
        self.message = message

        # check if we have a valid message
        if not self.is_valid_message():
            raise UnacceptableMessageException('Not an acceptable message type: {}'.format(type(self.message)))

        # 1. setup everything for sending
        self.setup()

        # 2. setup the exchange
        self.setup_exchange(self.message.exchange)

        # 3. publish the message to the broker
        status = self.publish(self.message.routing_key)

        # 4. tear down the connection
        self.tear_down()

        log.debug('Message sent.')
        return status

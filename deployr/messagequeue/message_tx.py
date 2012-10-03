# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import json
import socket
import pika
from pika import log
from pika.adapters.blocking_connection import BlockingConnection
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE, DEPLOY_CONFIRMATION_ROUTING_KEY
from config.queue_settings import BROKER_HOST
from config.queue_settings import BROKER_PORT
from ostools import OS_ERROR, OS_SUCCESS


##############################################################################
#
# callback chain
#
##############################################################################

def declare_exchange(channel):
    """
        Declaring exchange for sending the deployment confirmation messages
    """
    log.debug('Declaring exchange: {}'.format(GENAPI_DEPLOYMENT_EXCHANGE))
    channel.exchange_declare(
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        type='topic',
        durable=True,
        auto_delete=False
    )
    return channel


def enqueue_message(channel, queue_message):
    """
        Queue has been declared. Now start sending messages
        to the queue ...
    """
    log.info('Parsed message for JSON encoding: {}'.format(queue_message))
    try:
        json_message = json.dumps(queue_message)
    except ValueError, e:
        log.error('Cannot send message, it is not JSON parseable! Error: {}'.format(e))
        return OS_ERROR

    log.info("Sending message: {}".format(json_message))
    channel.basic_publish(
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        routing_key=DEPLOY_CONFIRMATION_ROUTING_KEY,
        body=json_message,
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )

    return OS_SUCCESS


##############################################################################
#
# main call methods
#
##############################################################################

def send_message(queue_message, broker_host=BROKER_HOST, broker_port=BROKER_PORT):
    """
        Sending a given message on DEPLOYMENT_QUEUE
    """
    global connection
    parameters = pika.ConnectionParameters(host=broker_host, port=broker_port)
    try:
        # create the connection
        connection = BlockingConnection(parameters)
        channel = connection.channel()

        # declare the queue to use
        log.debug("Declaring queue: {}".format(GENAPI_DEPLOYMENT_EXCHANGE))
        channel = declare_exchange(channel)
        log.info('Connected to broker: {}:{}'.format(broker_host, broker_port))

        # sending message
        enqueue_message(channel=channel, queue_message=queue_message)
    except socket.gaierror, e:
        log.error(e)
        return OS_ERROR
    except socket.error, e:
        log.error(e)
        return OS_ERROR
    except KeyboardInterrupt:
        log.info('Orderly shutting down ...')
        return OS_ERROR
    finally:
        if connection:
            connection.close()
            log.info('Connection closed.')

    return OS_SUCCESS

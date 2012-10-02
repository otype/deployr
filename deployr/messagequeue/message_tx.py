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
from config.queue_settings import GENAPI_DEPLOYMENT_QUEUE


##############################################################################
#
# callback chain
#
##############################################################################


def enqueue_message(channel, queue_message):
    """
        Queue has been declared. Now start to sendings messages
        to the queue ...
    """
    log.debug('Parsing message for JSON encoding: {}'.format(queue_message))
    try:
        json_message = json.dumps(queue_message)
    except ValueError, e:
        log.error('Cannot send message, it is not JSON parseable! Error: {}'.format(e))
        return

    log.info("Sending message: {}".format(json_message))
    channel.basic_publish(
        exchange='',
        routing_key=GENAPI_DEPLOYMENT_QUEUE,
        body=json_message,
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )

    # Close our connection
    connection.close()


##############################################################################
#
# main call methods
#
##############################################################################

def send_message(queue_message, broker_host='127.0.0.1', broker_port=5672):
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
        log.debug("Declaring queue: {}".format(GENAPI_DEPLOYMENT_QUEUE))
        channel.queue_declare(
            queue=GENAPI_DEPLOYMENT_QUEUE,
            durable=True,
            exclusive=False,
            auto_delete=False
        )
        log.info('Connected to broker: {}:{}'.format(broker_host, broker_port))

        # sending message
        enqueue_message(channel=channel, queue_message=queue_message)
    except socket.gaierror, e:
        log.error(e)
    except socket.error, e:
        log.error(e)
    except KeyboardInterrupt:
        log.info('Orderly shutting down ...')
    else:
        log.error('Unknown error! Better run away, now ...')
    finally:
        if connection:
            connection.close()
            log.info('Connection closed.')

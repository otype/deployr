# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import json
import socket
import pika
from pika import log
from pika.adapters.select_connection import SelectConnection
from config import MESSAGE_QUEUE_NAME


#
# Global connection object, used for connecting to the broker
#
from messagequeue.message_parser import parse_message

connection = None

#
# Global channel used in conjunction with the broker
#
channel = None

##############################################################################
#
# callback chain
#
##############################################################################


def on_connected(connection):
    """
        Callback method when connection to broker has been
        established.
    """
    global channel
    log.debug('Connected to Broker! Establishing channel.')
    connection.channel(on_channel_open)


def on_channel_open(channel_):
    """
        When opening the channel, we declare the queue to use
    """
    global channel
    channel = channel_
    log.debug("Declaring queue: {}".format(MESSAGE_QUEUE_NAME))
    channel.queue_declare(
        queue=MESSAGE_QUEUE_NAME,
        durable=True,
        exclusive=False,
        auto_delete=False,
        callback=on_queue_declared
    )


def on_queue_declared(frame):
    """
        Queue has been declared. Now start to consume messages
        from the queue ...
    """
    log.debug("Queue Declared")
    channel.basic_consume(handle_delivery, queue=MESSAGE_QUEUE_NAME)


def handle_delivery(channel, method_frame, header_frame, body):
    """
        Handle an incoming message.
    """
    log.info(
        "Received new task: content-type=\"%s\", delivery-tag=\"%i\", body=%s",
        header_frame.content_type,
        method_frame.delivery_tag,
        body
    )
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    try:
        json_body = json.loads(body)
        if json_body:
            parse_message(json_body)
    except ValueError, e:
        log.error('Could not identify message as JSON: {}! Error: {}'.format(body, e))
        # TODO: Send mail to admin that message error occurred


##############################################################################
#
# main call methods
#
##############################################################################


def start_consumer(broker_host='127.0.0.1', broker_port=5672):
    global connection
    parameters = pika.ConnectionParameters(host=broker_host, port=broker_port)
    try:
        connection = SelectConnection(parameters, on_connected)
        log.info('Connected to broker: {}:{}'.format(broker_host, broker_port))
        connection.ioloop.start()
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

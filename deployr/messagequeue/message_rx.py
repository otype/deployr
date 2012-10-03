# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import socket
import pika
from pika import log
from pika.adapters.select_connection import SelectConnection
from task.task_execution import run_task
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE
from config.queue_settings import DEPLOY_ROUTING_KEY
from config.queue_settings import GENAPI_DEPLOYMENT_QUEUE
from config.queue_settings import BROKER_HOST
from config.queue_settings import BROKER_PORT


#
# Global connection object, used for connecting to the broker
#
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
    log.debug('Connected to Broker! Establishing channel.')
    connection.channel(on_channel_open)


def on_channel_open(channel_):
    """
        When opening the channel, we declare the queue to use
    """
    global channel
    channel = channel_

    log.debug("Declaring exchange: {}".format(GENAPI_DEPLOYMENT_EXCHANGE))
    channel.exchange_declare(
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        type='topic',
        durable=True,
        auto_delete=False
    )

    log.debug("Declaring queue: {}".format(GENAPI_DEPLOYMENT_QUEUE))
    channel.queue_declare(
        queue=GENAPI_DEPLOYMENT_QUEUE,
        callback=on_queue_declared,
        durable=True,
        exclusive=False,
        auto_delete=False
    )


def on_queue_declared(frame):
    """
        Queue has been declared. Now start to consume messages
        from the queue ...
    """
    log.debug("Consuming message from exchange=\'{}\' running on queue=\'{}\'".format(
        GENAPI_DEPLOYMENT_EXCHANGE, GENAPI_DEPLOYMENT_QUEUE)
    )
    log.info('Frame: {}'.format(frame))

    log.debug('Binding to queue: {}'.format(GENAPI_DEPLOYMENT_QUEUE))
    channel.queue_bind(
        callback=on_queue_bound,
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        queue=GENAPI_DEPLOYMENT_QUEUE,
        routing_key=DEPLOY_ROUTING_KEY
    )


def on_queue_bound(frame):
    """
        Queue is bound! Now start consuming!
    """
    log.debug('Queue \'{}\' bound!'.format(GENAPI_DEPLOYMENT_QUEUE))
    log.debug('Frame: {}'.format(frame))
    channel.basic_consume(consumer_callback=handle_delivery, queue=GENAPI_DEPLOYMENT_QUEUE)


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
    log.debug('Acknowledging received message.')
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    # Run the task from parsed message
    run_task(body)


##############################################################################
#
# main call methods
#
##############################################################################


def start_consumer(broker_host=BROKER_HOST, broker_port=BROKER_PORT):
    """
        Start the consumer IOLoop
    """
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

# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import socket
import pika
from comms.messagequeue.queue_settings import GENAPI_DEPLOYMENT_QUEUE
from config.logging_configuration import logger as log
from pika.adapters.select_connection import SelectConnection
from support.ostools import OS_SUCCESS
from support.task.task_execution import run_task


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

    log.debug("Declaring queue: {}".format(GENAPI_DEPLOYMENT_QUEUE))
    channel.queue_declare(
        queue=GENAPI_DEPLOYMENT_QUEUE,
        callback=on_queue_declared,
        durable=True,
        exclusive=False,
        auto_delete=False
    )


#def set_prefetch_count():
#    """
#        Only accepting one message at a time ...
#    """
#    prefetch_count = 1
#    log.debug('Setting prefetch_count = {}'.format(prefetch_count))
#    channel.basic_qos(prefetch_count=prefetch_count)


def on_queue_declared(frame):
    """
        Queue has been declared. Now start to consume messages
        from the queue ...
    """
    log.debug("Consuming message from queue=\'{}\'".format(GENAPI_DEPLOYMENT_QUEUE))
    log.debug('Frame: {}'.format(frame))

#    if activate_prefetch_count:
#        set_prefetch_count()

    log.debug('Now consuming from broker.')
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

    # Run the task from parsed message
    status = run_task(body)
    if status == OS_SUCCESS:
        log.debug('Acknowledging received message.')
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        log.error('Error running task!')


##############################################################################
#
# main call methods
#
##############################################################################


def start_consumer(broker_host, broker_port, username, password, activate_prefetch):
    """
        Start the consumer IOLoop
    """
    global connection
#    global activate_prefetch_count
#
#    activate_prefetch_count = activate_prefetch

    credentials = pika.PlainCredentials(username=username, password=password)
    parameters = pika.ConnectionParameters(host=broker_host, port=broker_port, credentials=credentials)
    try:
        connection = SelectConnection(parameters, on_connected)
        log.info('Connected to broker: {}:{}'.format(broker_host, broker_port))
        connection.ioloop.start()
    except socket.gaierror, e:
        log.error("Socket.gaierror! Error: {}".format(e))
        if connection:
            connection.close()
    except socket.error, e:
        log.error("Socket.error! Error: {}".format(e))
        if connection:
            connection.close()
    except KeyboardInterrupt:
        log.info('Orderly shutting down ...')
        connection.close()
    except Exception, e:
        log.error('Unknown error! Better run away, now! Error: {}'.format(e))
    finally:
        log.info('Connection closed.')

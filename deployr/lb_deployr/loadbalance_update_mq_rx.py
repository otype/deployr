# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import logging
import socket
import pika
from pika.adapters.select_connection import SelectConnection
from deployrlib.globals.queue_settings import LOADBALANCE_UPDATE_QUEUE
from deployrlib.globals.return_codes import OS_SUCCESS
from deployrlib.services import task_service



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
    logging.debug('Connected to Broker! Establishing channel.')
    connection.channel(on_channel_open)


def on_channel_open(channel_):
    """
        When opening the channel, we declare the queue to use
    """
    global channel
    channel = channel_

    logging.debug("Declaring queue: {}".format(LOADBALANCE_UPDATE_QUEUE))
    channel.queue_declare(
        queue=LOADBALANCE_UPDATE_QUEUE,
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
#    logging.debug('Setting prefetch_count = {}'.format(prefetch_count))
#    channel.basic_qos(prefetch_count=prefetch_count)


def on_queue_declared(frame):
    """
        Queue has been declared. Now start to consume messages
        from the queue ...
    """
    logging.debug("Consuming message from queue=\'{}\'".format(LOADBALANCE_UPDATE_QUEUE))
    logging.debug('Frame: {}'.format(frame))

#    if activate_prefetch_count:
#        set_prefetch_count()

    logging.debug('Now consuming from broker.')
    channel.basic_consume(consumer_callback=handle_delivery, queue=LOADBALANCE_UPDATE_QUEUE)


def handle_delivery(channel, method_frame, header_frame, body):
    """
        Handle an incoming message.
    """
    logging.info(
        "Received new task: content-type=\"%s\", delivery-tag=\"%i\", body=%s",
        header_frame.content_type,
        method_frame.delivery_tag,
        body
    )

    # Run the task from parsed message
    status = task_service.run_task(body)
    if status == OS_SUCCESS:
        logging.debug('Acknowledging received message.')
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        logging.error('Error running task!')


##############################################################################
#
# main call methods
#
##############################################################################


def start_consumer(broker_host, broker_port, username, password, activate_prefetch=None):
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
        logging.info('Connected to broker: {}:{}'.format(broker_host, broker_port))
        connection.ioloop.start()
    except socket.gaierror, e:
        logging.error("Socket.gaierror! Error: {}".format(e))
        if connection:
            connection.close()
    except socket.error, e:
        logging.error("Socket.error! Error: {}".format(e))
        if connection:
            connection.close()
    except KeyboardInterrupt:
        logging.info('Orderly shutting down ...')
        connection.close()
    except Exception, e:
        logging.error('Unknown error! Better run away, now! Error: {}'.format(e))
    finally:
        logging.info('Connection closed.')

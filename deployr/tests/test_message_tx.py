# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
import pika
from pika.adapters.blocking_connection import BlockingConnection
from messagequeue.message_tx import enqueue_message, send_message


def setup_func():
    parameters = pika.ConnectionParameters()

    global connection
    connection = BlockingConnection(parameters)
    assert connection

    global channel
    channel = connection.channel()
    assert channel


def teardown_func():
    connection.close()


@with_setup(setup_func, teardown_func)
def test_enqueue_message():
    message = {"testing": "stuff"}
    try:
        # This is deprecated, therefore we are expecting a TypeError
        enqueue_message(channel=channel, queue_message=message)
    except TypeError:
        return True
    else:
        return False


@with_setup(setup_func, teardown_func)
def test_send_message():
    message = {"testing": "stuff"}
    try:
        # This is deprecated, therefore we are expecting a TypeError
        send_message(queue_message=message)
    except TypeError:
        return True
    else:
        return False

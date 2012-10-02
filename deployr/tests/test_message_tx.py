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
from ostools import OS_SUCCESS


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
    assert OS_SUCCESS == enqueue_message(channel=channel, queue_message=message)


@with_setup(setup_func, teardown_func)
def test_send_message():
    message = {"testing": "stuff"}
    assert OS_SUCCESS == send_message(queue_message=message)

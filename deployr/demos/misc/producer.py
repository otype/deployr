# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import pika
import sys
from config.queue_settings import GENAPI_DEPLOYMENT_QUEUE

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=GENAPI_DEPLOYMENT_QUEUE, durable=True)

deploy_message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
    routing_key=GENAPI_DEPLOYMENT_QUEUE,
    body=deploy_message,
    properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
    ))
print " [x] Sent %r" % (deploy_message,)
connection.close()
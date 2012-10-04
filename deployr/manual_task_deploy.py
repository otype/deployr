# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys
import pika
from pika import log
from config.queue_settings import DEPLOY_ROUTING_KEY
from config.queue_settings import GENAPI_DEPLOYMENT_EXCHANGE
from task.messages.deploy_message import DeployMessage

def deploy_message():
    return DeployMessage(
        api_id='aoisdf8hjsd9vh8',
        db_host='riak1.apitrary.net',
        db_port=8098,
        genapi_version=1,
        log_level='debug',
        entities=['users', 'dogs'],
        api_key='aksdfj09sdfj0sdjf09sjd0jsdv0js0dvj'
    )


def connect(host):
    log.info("Sending to host: {}".format(host))
    parameters = pika.ConnectionParameters(host)
    connection = pika.BlockingConnection(parameters)
    log.info(connection.parameters.host)
    log.info(connection.parameters.port)

    channel = connection.channel()
    channel.exchange_declare(
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        type='topic',
        durable=True,
        auto_delete=False
    )
    return connection, channel


def publish(connection, channel, message):
    log.info('Publishing on exchange: {} with routing key: {}'.format(GENAPI_DEPLOYMENT_EXCHANGE, DEPLOY_ROUTING_KEY))
    channel.basic_publish(
        exchange=GENAPI_DEPLOYMENT_EXCHANGE,
        routing_key=DEPLOY_ROUTING_KEY,
        body=message,
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )
    log.info("Sent %r:%r" % (DEPLOY_ROUTING_KEY, message))
    connection.close()


def main(host):
    connection, channel = connect(host)
    publish(connection=connection, channel=channel, message=deploy_message().to_json())


if __name__ == '__main__':
    host = (len(sys.argv) > 1) and sys.argv[1] or '127.0.0.1'
    main(host)

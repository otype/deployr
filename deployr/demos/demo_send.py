import json
import sys
import pika
from pika import log
from messagequeue.message_rx import SelectConnection

pika.log.setup(color=True)

connection = None
channel = None

queue = 'GENAPI_DEPLOYMENT'
deploy_message = {
    'task_type': 'DEPLOY',
    'api_id': '88sdhv98shdvlh123',
    'db_host': 'db1.apitrary.net',
    'db_port': 8098,
    'genapi_version': 1,
    'log_level': 'debug',
    'entities': ['user', 'object', 'contact'],
    'api_key': 'iis9nd9vnsdvoijsdvoin9s8dv',
    'api_access_key': 'jjjoindv08988v88dh'
}


# Import all adapters for easier experimentation
from pika.adapters import *


def on_connected(connection):
    pika.log.info("demo_send: Connected to RabbitMQ")
    connection.channel(on_channel_open)


def on_channel_open(channel_):
    global channel
    channel = channel_
    pika.log.info("demo_send: Received our Channel")
    channel.queue_declare(queue=queue, durable=True, exclusive=False, auto_delete=False, callback=on_queue_declared)


def on_queue_declared(frame):
    pika.log.info("demo_send: Queue Declared")
    message = json.dumps(deploy_message)
    pika.log.info("Sending: %s" % message)
    channel.basic_publish(
        exchange='',
        routing_key=queue,
        body=message,
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )

    # Close our connection
    connection.close()

if __name__ == '__main__':
    host = (len(sys.argv) > 1) and sys.argv[1] or '127.0.0.1'
    parameters = pika.ConnectionParameters(host)
    connection = SelectConnection(parameters, on_connected)
    try:
        connection.ioloop.start()
    except KeyboardInterrupt:
        connection.close()
        connection.ioloop.start()

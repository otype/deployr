import json
import sys
import pika
from pika import log
import time


pika.log.setup(color=True)

connection = None
channel = None

exchange_name = 'genapi_deployment_exchange'
deploy_message = {
    'task_type': 'DEPLOY',
    'api_id': '88sdhv98shdvlh123',
    'db_host': 'riak1.apitrary.net',
    'db_port': 8098,
    'genapi_version': 1,
    'log_level': 'debug',
    'entities': ['user', 'object', 'contact'],
    'api_key': 'iis9nd9vnsdvoijsdvoin9s8dv'
}

confirmation_message = {
    'task_type': 'DEPLOY_CONFIRMATION',
    'api_id': '88sdhv98shdvlh123',
    'genapi_version': 1,
    'host': 'app2.apitrary.net',
    'port': 8769,
    'status': 1,
    'created_at': time.time()
}


if __name__ == '__main__':
    host = (len(sys.argv) > 1) and sys.argv[1] or '127.0.0.1'
    log.info("Sending to host: {}".format(host))
    parameters = pika.ConnectionParameters(host)
    connection = pika.BlockingConnection(parameters)
    log.info(connection.parameters.host)
    log.info(connection.parameters.port)
    channel = connection.channel()
    channel.exchange_declare(
        exchange=exchange_name,
        type='topic',
        durable=True,
        auto_delete=False
    )

    routing_key = 'apitrary.genapi.deploy.request'
    log.info('Publishing on exchange: {} with routing key: {}'.format(exchange_name, routing_key))
    channel.basic_publish(
        exchange=exchange_name,
        routing_key=routing_key,
        body=json.dumps(deploy_message),
        properties=pika.BasicProperties(content_type="application/json", delivery_mode=2)
    )

    log.info("Sent %r:%r" % (routing_key, deploy_message))
    connection.close()

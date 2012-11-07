# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys
from config.config_manager import load_configuration
from config.logging_configuration import logger as log
from messagequeue.blocking_message_tx import BlockingMessageTx
from task.messages.deploy_message import DeployMessage

msg = DeployMessage(
    api_id='aoisdf8hjsd9vh8',
    db_host='riak1.apitrary.net',
    db_port=8098,
    genapi_version=1,
    log_level='debug',
    entities=['users', 'dogs'],
    api_key='aksdfj09sdfj0sdjf09sjd0jsdv0js0dvj'
)

# Load the global configuration from config file
config = load_configuration()

def send(host, message):
    """
        Simply send the message
    """
    config['BROKER_HOST'] = host
    message_tx = BlockingMessageTx(config=config)
    message_tx.send(message=message)

# MAIN
#
#
if __name__ == '__main__':
    host = (len(sys.argv) > 1) and sys.argv[1] or '127.0.0.1'
    log.info('Connecting to broker: {}'.format(host))

    log.info('Sending message from manual task deploy script')
    send(host=host, message=msg)

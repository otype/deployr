# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys
from comms.messagequeue.blocking_message_tx import BlockingMessageTx
from config.config_manager import load_configuration
from config.logging_configuration import logger as log
from deploy.deploy_message import DeployMessage

msg = DeployMessage(
    api_id='aaaaaaaaaaaaaaaaaaaaaaaaaaa',
    db_host='riak1.dev.apitrary.net',
    db_port=8098,
    genapi_version=1,
    log_level='debug',
    entities=['jedis', 'wookies', 'stormtroopers'],
    api_key='suchasecretapikeyyouwouldneverguess'
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

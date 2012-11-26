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
from features.loadbalance_update.loadbalance_update_message import LoadbalanceUpdateMessage

msg = LoadbalanceUpdateMessage(
    api_id='aaaaaaaaaaaaaaaaaaaaaaaaaaa',
    api_host='app1.dev.apitrary.net',
    api_port=9999      # THIS IS FAKE AND NEEDS TO BE FIXED!
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

    log.info('Sending message from manual loadbalance update script')
    send(host=host, message=msg)

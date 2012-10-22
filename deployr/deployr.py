#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import argparse
import pika
from pika import log
from config.default_configuration import LOGGING_LEVEL
from config.environment import CURRENT_CONFIGURATION

##############################################################################
#
# GENERAL CONFIGURATION + SHELL PARAMETER DEFINITIONS
#
##############################################################################

# Default log level
pika.log.setup(pika.log.INFO, color=True)

##############################################################################
#
# FUNCTIONS
#
##############################################################################


def show_all_settings():
    """
        Show all configured constants
    """
    log.info('Starting service: deployr')
    log.info('Remote Broker: {}:{}'.format(args.broker_host, args.broker_port))
    log.info('Deployr mode: {}'.format(args.mode))
    log.info('Environment: {}'.format(CURRENT_CONFIGURATION['NAME']))

    config_to_show = str(CURRENT_CONFIGURATION)
    config_to_show = config_to_show.replace(CURRENT_CONFIGURATION['BROKER_PASSWORD'], '<hidden>')
    config_to_show = config_to_show.replace(CURRENT_CONFIGURATION['SUPERVISOR_XML_RPC_USERNAME'], '<hidden>')
    config_to_show = config_to_show.replace(CURRENT_CONFIGURATION['SUPERVISOR_XML_RPC_PASSWORD'], '<hidden>')

    log.info('Configuration: {}'.format(config_to_show))
    log.info('Logging level: {}'.format(args.logging))


def set_log_level(log_level):
    """
        Sets the log level (use colored logging output).
        This is a wrapper for python logging.
    """
    if log_level.lower() == LOGGING_LEVEL.DEBUG:
        pika.log.setup(pika.log.DEBUG, color=True)
    elif log_level.lower() == LOGGING_LEVEL.WARN:
        pika.log.setup(pika.log.WARNING, color=True)
    else:
        pika.log.setup(pika.log.INFO, color=True)


def parse_shell_args():
    """
        Parse the shell arguments
    """
    global args
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-B",
        "--broker_host",
        help="Hostname or IP of the broker",
        type=str,
        default=CURRENT_CONFIGURATION['BROKER_HOST']
    )

    parser.add_argument(
        "-P",
        "--broker_port",
        help="Port of the broker",
        type=int,
        default=CURRENT_CONFIGURATION['BROKER_PORT']
    )

    parser.add_argument(
        "-L",
        "--logging",
        help="Logging level",
        type=str,
        choices=[LOGGING_LEVEL.DEBUG, LOGGING_LEVEL.INFO, LOGGING_LEVEL.WARN],
        default=CURRENT_CONFIGURATION['LOGGING']
    )

    parser.add_argument(
        "-M",
        "--mode",
        help="Deployr mode",
        type=str,
        choices=['deploy', 'balance'],
        default='deploy'
    )

    args = parser.parse_args()


def main():
    """
        Start the Tornado Web server
    """
    # Parse the shell arguments, first.
    parse_shell_args()

    # Show all configured handlers
    show_all_settings()

    # Set the log level
    set_log_level(args.logging)

    # Queue credentials
    username = CURRENT_CONFIGURATION['BROKER_USER']
    password = CURRENT_CONFIGURATION['BROKER_PASSWORD']

    # start the MQ consumer
    if args.mode == 'deploy':
        from messagequeue.deployment_rx import start_consumer
    elif args.mode == 'balance':
        from messagequeue.loadbalance_update_rx import start_consumer
    else:
        from messagequeue.loadbalance_update_rx import start_consumer

    start_consumer(
        broker_host=args.broker_host,
        broker_port=args.broker_port,
        username=username,
        password=password
    )

##############################################################################
#
# MAIN
#
##############################################################################

if __name__ == '__main__':
    main()

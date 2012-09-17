#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import argparse
import pika
from pika import log
from messagequeue.message_rx import start_consumer

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
        Show all configured settings
    """
    log.info('Starting service: deployr')
    log.info('Remote Broker: {}:{}'.format(args.broker_host, args.broker_port))
    log.info('Environment: {}'.format(args.env))
    log.info('Logging level: {}'.format(args.logging))


def set_log_level(log_level):
    """
        Sets the log level (use colored logging output).
        This is a wrapper for python logging.
    """
    if log_level.lower() == "debug":
        pika.log.setup(pika.log.DEBUG, color=True)
    else:
        pika.log.setup(pika.log.INFO, color=True)


def parse_shell_args():
    """
        Parse the shell arguments
    """
    global args
    parser = argparse.ArgumentParser()

    parser.add_argument("-B", "--broker_host", help="Hostname or IP of the broker", type=str, default='127.0.0.1')
    parser.add_argument("-P", "--broker_port", help="Port of the broker", type=int, default=5672)
    parser.add_argument("-E", "--env", help="Environment to run in", type=str, choices=['dev', 'live'], default='dev')
    parser.add_argument("-L", "--logging", help="Logging level", type=str, choices=['debug', 'info'], default='info')

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

    # start the MQ consumer
    start_consumer(broker_host=args.broker_host, broker_port=args.broker_port)

##############################################################################
#
# MAIN
#
##############################################################################

if __name__ == '__main__':
    main()

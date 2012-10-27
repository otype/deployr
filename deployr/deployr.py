#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import argparse
import pika
from pika import log
import sys
from config.config_manager import strip_out_sensitive_data, load_configuration, write_configuration
from config.default_configuration import LOGGING_LEVEL, ENVIRONMENT

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


def show_all_settings(config):
    """
        Show all configured constants
    """
    log.info('Starting service: deployr')
    log.info('Remote Broker: {}:{}'.format(config['BROKER_HOST'], config['BROKER_PORT']))
    log.info('Deployr mode: {}'.format(args.mode))
    log.info('Environment: {}'.format(config['NAME']))

    config_to_show = strip_out_sensitive_data(config)
    log.info('Configuration: {}'.format(config_to_show))
    log.info('Logging level: {}'.format(config['LOGGING']))


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
        "-M",
        "--mode",
        help="Deployr mode",
        type=str,
        choices=['deploy', 'balance'],
        default='deploy'
    )

    parser.add_argument(
        "-w",
        "--write_config",
        help="Write the configuration file",
        type=str,
        choices=[ENVIRONMENT.DEV, ENVIRONMENT.LIVE]
    )

    args = parser.parse_args()


def check_for_config_write():
    """
        Write configuration file if called via shell param
    """
    config_env = args.write_config
    write_configuration(config_env)
    log.info("Configuration file written! Now, edit config file and start deployr!")
    sys.exit(0)


def main():
    """
        Start the Tornado Web server
    """
    # Parse the shell arguments, first.
    parse_shell_args()

    # Check if config write has been requested. If yes, bail out afterwards.
    if args.write_config:
        check_for_config_write()

    # Load configuration
    config = load_configuration()

    # Show all configured handlers
    show_all_settings(config)

    # Set the log level
    set_log_level(config['LOGGING'])

    # start the MQ consumer
    if args.mode == 'deploy':
        from messagequeue.deployment_rx import start_consumer
    elif args.mode == 'balance':
        from messagequeue.loadbalance_update_rx import start_consumer
    else:
        from messagequeue.deployment_rx import start_consumer

    start_consumer(
        broker_host=config['BROKER_HOST'],
        broker_port=int(config['BROKER_PORT']),
        username=config['BROKER_USER'],
        password=config['BROKER_PASSWORD'],
        activate_prefetch=config['BROKER_PREFETCH_COUNT']
    )

##############################################################################
#
# MAIN
#
##############################################################################

if __name__ == '__main__':
    main()

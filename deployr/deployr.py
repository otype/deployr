#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import argparse
import logging
import sys
from deployrlib.models.environments import ENVIRONMENT
from deployrlib.services import deployr_config_service, logging_service


##############################################################################
#
# FUNCTIONS
#
##############################################################################


def show_all_settings(config):
    """
        Show all configured constants
    """
    logging.info('Starting service: deployr')
    logging.info('Remote Broker: {}:{}'.format(config['BROKER_HOST'], config['BROKER_PORT']))
    logging.info('Deployr mode: {}'.format(args.mode))
    logging.info('Environment: {}'.format(config['NAME']))

    config_to_show = deployr_config_service.strip_out_sensitive_data(config)
    logging.info('Configuration: {}'.format(config_to_show))
    logging.info('Logging level: {}'.format(config['LOGGING']))


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
    deployr_config_service.write_configuration(config_env)
    logging.info("Configuration file written! Now, edit config file and start deployr!")
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
    config = deployr_config_service.load_configuration()

    # Show all configured handlers
    show_all_settings(config)

    # Set the app-wide logging level
    # TODO: Set this correctly! Otherwise we have messed up logging.
    log_level = logging_service.get_log_level_from_config(config['LOGGING'])
    log = logging_service.setup_logging(log_level)

    # start the MQ consumer
    if args.mode == 'deploy':
        from app_deployr.deploy_mq_rx import start_consumer
    elif args.mode == 'balance':
        from lb_deployr.loadbalance_update_mq_rx import start_consumer
    else:
        from app_deployr.deploy_mq_rx import start_consumer

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

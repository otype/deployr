# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
import logging
import socket

##############################################################################
#
# helper functions
#
##############################################################################


##############################################################################
#
# main call methods
#
##############################################################################


def get_open_port():
    """
        Responsible for getting a free port.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    logging.debug('Port {} is available.'.format(port))
    return port

# -*- coding: utf-8 -*-
"""

    <application_name>

    by hgschmidt

    Copyright (c) 2012 apitrary

"""

#
# Message Queue name
#
# This here is crucial:
# The deployr will listen to the broker but will only accept messages
# on this queue (a work queue using round-robin/fair-dispatch message
# distribution).
#
# DO NOT CHANGE THIS HERE WITHOUT THOUGHT!
GENAPI_DEPLOYMENT_QUEUE = 'GENAPI_DEPLOYMENT'

# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""

#
# Application details
#
APP_DETAILS = {
    'name': 'deployr',
    'version': '0.1',
    'company': 'apitrary',
    'support': 'http://apitrary.com/support',
    'contact': 'support@apitrary.com',
    'copyright': '2012 apitrary.com'
}


#
# Message Queue name
#
# This here is crucial:
# The deployr will listen to the broker but will only accept messages
# on this queue (a work queue using round-robin/fair-dispatch message
# distribution).
#
# DO NOT CHANGE THIS HERE WITHOUT THOUGHT!
MESSAGE_QUEUE_NAME = 'GENAPI_DEPLOYMENT'

# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys

# SUPERVISORD HOST
#
# On which host to find the supervisord. This should always
# be 'localhost' except for debugging/development reasons.
if sys.platform == 'darwin':
    SUPERVISORD_HOST = 'apis1.live.apitrary.net'
elif sys.platform == 'linux2':
    SUPERVISORD_HOST = '127.0.0.1'
else:
    SUPERVISORD_HOST = '127.0.0.1'

# SUPERVISORD WEB PORT
#
# XML-RPC web API of a running supervisord.
# NEEDS TO BE ACTIVATED IN THE CONFIGS!
SUPERVISORD_WEB_PORT = 9001

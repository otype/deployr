# -*- coding: utf-8 -*-
"""

    deployr

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import sys

# Configuration file for deployr
#
#
if sys.platform == 'darwin':
    DEPLOYR_CONFIG_FILE = 'deployr.conf'
elif sys.platform == 'linux2':
    DEPLOYR_CONFIG_FILE = '/etc/deployr/deployr.conf'
else:
    DEPLOYR_CONFIG_FILE = 'deployr.conf'


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    usage: sudo python setup.py install

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import os
import sys
from distutils.core import setup
from setuptools import find_packages
from deployr.config.general_settings import __version__
from deployr.config.general_settings import __name__
from deployr.config.general_settings import __author__

required = ['pika', 'jinja2', 'nose']

# Read the $HOME variable! Overwrite it if we're on Windows.
HOME = os.getenv('HOME')
if sys.platform == 'win32':
    HOME = os.path.expanduser('~')

# Extra options can be set here without cluttering the setup() method.
extra_options = dict(
    # Nothing
)

setup(
    name=__name__,
    version=__version__,
    description='deployr',
    author=__author__,
    author_email='hgs@apitrary.com',
    url='https://apitrary.com',
    install_requires=required,
    packages=find_packages('deployr'),
    package_dir={'' : 'deployr'},
    scripts=['start.py'],
    data_files=None,
    download_url='',
    license='Apache 2.0',
    **extra_options
)

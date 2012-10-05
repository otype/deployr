#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    deployr

    usage: sudo python setup.py install

    by hgschmidt

    Copyright (c) 2012 apitrary

"""
import os
from distutils.core import setup
from setuptools import find_packages
from deployr.config.general_settings import __version__
from deployr.config.general_settings import __name__
from deployr.config.general_settings import __author__
from deployr.config.general_settings import __author_email__
from deployr.config.general_settings import __url__

# List of required libraries
required = ['pika', 'jinja2', 'nose']

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=__name__,
    version=__version__,
    description='deployr',
    author=__author__,
    author_email=__author_email__,
    description = ('apitrary\'s deployr - the application node manager for GenAPIs'),
    long_description=read('README.md'),
    url=__url__,
    install_requires=required,
    keywords='deployr node manager apitrary application',
    packages=find_packages('deployr'),
#    package_dir={'': 'deployr'},
    scripts=['deployr/start.py'],
#    data_files=None,
    download_url='',
    license='copyright'
)

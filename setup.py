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
from constants.general_settings import __version__
from constants.general_settings import __name__
from constants.general_settings import __author__
from constants.general_settings import __author_email__
from constants.general_settings import __url__


def read(fname):
    """
        Read the README.md file
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requirements():
    """
        Read the requirements.txt file
    """
    with open('requirements.txt') as f:
        requirements = f.readlines()
    return [element.strip() for element in requirements]


setup(
    name=__name__,
    version=__version__,
    description='deployr',
    author=__author__,
    author_email=__author_email__,
    description=('apitrary\'s deployr - the application node manager for GenAPIs'),
    long_description=read('README.md'),
    url=__url__,
    install_requires=read_requirements(),
    keywords='deployr node manager apitrary application',
    packages=find_packages('deployr'),
    scripts=['deployr/deployr.py']
)

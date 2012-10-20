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
    name='deployr',
    version='0.1',
    author='Hans-Gunther Schmidt',
    author_email='hgs@apitrary.com',
    description='apitrary deployr - the application node manager for GenAPIs',
    long_description=read('README.md'),
    url='http://apitrary.com',
    install_requires=read_requirements(),
    keywords='deployr node manager apitrary application',
    packages=find_packages('deployr'),
    scripts=['deployr/deployr.py']
)

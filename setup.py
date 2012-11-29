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
import sys


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


def scripts_list():
    return [
        'deployr/deployr.py',
        'deployr/app_deployr/manual_task_deploy.py'
        'deployr/lb_deployr/manual_task_loadbalance_update.py'
    ]


def get_template_base_dir():
    if sys.platform == 'darwin':
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))
    elif sys.platform == 'linux2':
        template_dir = "/etc/deployr/templates"
    else:
        template_dir = "{}/.deployr/templates".format(os.getenv("HOME"))

    return template_dir


setup(
    name='deployr',
    version='0.4.0',
    author='Hans-Gunther Schmidt',
    author_email='hgs@apitrary.com',
    description='apitrary deployr - the application node manager for GenAPIs',
    long_description=read('README.md'),
    url='http://apitrary.com',
    install_requires=read_requirements(),
    keywords='deployr node manager apitrary application',
    packages=find_packages('deployr'),
    package_dir={'': 'deployr'},
    data_files=[
        (get_template_base_dir(), ['app_deployr/templates/genapi_base.tpl']),
        (get_template_base_dir(), ['lb_deployr/templates/genapi_backends.tpl']),
        (get_template_base_dir(), ['lb_deployr/templates/genapi_frontends.tpl'])
    ],
    scripts=scripts_list()
)

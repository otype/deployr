# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
import os
from deployrlib.config.template_config import GENAPI_TEMPLATES_CONFIG
from deployrlib.repositories.template_repository import entity_list_as_csv, load_template
from deployrlib.services.filesystem_service import write_file

API_ID = 'abc123abc123abc123abc123'

GENAPI_CONFIG = """[program:abc123abc123abc123abc123]
command=/usr/bin/python /usr/bin/genapi_runner.py --logging=debug --riak_host=riak1.dev.apitrary.net --port=50000 --api_id=abc123abc123abc123abc123 --api_version=1 --env=dev --entity=users,contacts --api_key=secretkeysecretkey
directory=/home/genapi
user=genapi
autorestart=true
redirect_stderr=true
stdout_logfile=/home/genapi/abc123abc123abc123abc123.log
loglevel=info"""


tpl = ''

def setup_func():
    # Load the template
    template = load_template(GENAPI_TEMPLATES_CONFIG['GENAPI_BASE']['GENAPI_BASE_TEMPLATE'])

    # Render the template with substituted values
    global tpl
    tpl = template.render(
        python_interpreter='/usr/bin/python',
        genapi_start='/usr/bin/genapi_runner.py',
        logging_level='debug',
        riak_host='riak1.dev.apitrary.net',
        app_port=50000,
        genapi_api_id='abc123abc123abc123abc123',
        genapi_version=1,
        genapi_env='dev',
        genapi_entity_list=entity_list_as_csv(['users', 'contacts']),
        genapi_api_key='secretkeysecretkey',
        genapi_home_directory='/home/genapi',
        genapi_user='genapi',
        genapi_log_file='/home/genapi/abc123abc123abc123abc123.log',
        config_file_name='abc123abc123abc123abc123.conf'
    )


def teardown_func():
    if os.path.exists('{}.conf'.format(API_ID)):
        os.remove('{}.conf'.format(API_ID))


@with_setup(setup_func, teardown_func)
def test_genapi_template():
    assert tpl == GENAPI_CONFIG


@with_setup(setup_func, teardown_func)
def test_writer_file():
    write_file(filename='{}.conf'.format(API_ID), content=tpl)
    assert os.path.exists('{}.conf'.format(API_ID))


@with_setup(setup_func, teardown_func)
def test_entity_list_as_csv():
    arr = ['1', '2', '3']
    comp = '1,2,3'
    assert comp == entity_list_as_csv(arr)

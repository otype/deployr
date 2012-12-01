# -*- coding: utf-8 -*-
"""

    deployr

    Copyright (c) 2012 apitrary

"""
from nose.tools.nontrivial import with_setup
import os
from deployrlib.repositories.template_repository import entity_list_as_csv
from deployrlib.services.filesystem_service import write_file

API_ID = '88sdhv98shdvlh123'

GENAPI_CONFIG = """[program:88sdhv98shdvlh123]
command=/Users/hgschmidt/Development/virtualenvs/rmq/bin/python /opt/genapis/genapi/start.py --logging=debug --riak_host=db1.apitrary.net --port=50702 --api_id=88sdhv98shdvlh123 --api_version=1 --entity=user,object,contact
directory=/opt/genapi
user=genapi
autorestart=true
redirect_stderr=true
stdout_logfile=/opt/genapis/genapi_88sdhv98shdvlh123.log
loglevel=info"""


def setup_func():
    global tpl
    tpl = ''
    # TODO: Fix this! genapi_base_template was removed!
#    tpl = genapi_base_template(
#        genapi_api_id='88sdhv98shdvlh123',
#        python_interpreter='/Users/hgschmidt/Development/virtualenvs/rmq/bin/python',
#        genapi_start='/opt/genapis/genapi/start.py',
#        logging_level='debug',
#        riak_host='db1.apitrary.net',
#        app_port=50702,
#        genapi_version=1,
#        genapi_entity_list=['user', 'object', 'contact'],
#        genapi_home_directory='/opt/genapi',
#        genapi_user='genapi',
#        genapi_log_file='/opt/genapis/genapi_88sdhv98shdvlh123.log'
#    )


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

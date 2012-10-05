#!/bin/bash

CWD=`dirname $0`
PY_EXEC=`which python`

$PY_EXEC $CWD/deployr/deployr.py $*

#!/bin/bash
set -e
SCRIPT_ROOT=`dirname "${BASH_SOURCE[0]}"`

source ${SCRIPT_ROOT}/.venv/bin/activate
exec ${SCRIPT_ROOT}/manage.py $@
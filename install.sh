#!/bin/bash
echo "Script executed from: ${PWD}"
BASEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "Script location: ${BASEDIR}"
pip install -r requirements.txt
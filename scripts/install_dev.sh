#!/usr/bin/env bash

set -e

cd "$( dirname "${BASH_SOURCE[0]}" )/.." || exit

python -m pip install -r requirements.txt -r requirements-dev.txt -e .

#!/usr/bin/env bash
CURRENT_DIRPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

/bin/bash "${CURRENT_DIRPATH}/install_dev.sh"
pytest "${CURRENT_DIRPATH}/../retail_calc_demo/tests" -vv
pylint --rcfile="${CURRENT_DIRPATH}/../.pylintrc" retail_calc_demo
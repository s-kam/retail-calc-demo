#!/usr/bin/env bash
set -e
cd "$( dirname "${BASH_SOURCE[0]}" )/.." || exit

FILENAMES=$(find . -maxdepth 1 -name "requirements*.in" | sort -r)
for filename in ${FILENAMES}
do
  pip-compile -v -r -U "${filename}"
done

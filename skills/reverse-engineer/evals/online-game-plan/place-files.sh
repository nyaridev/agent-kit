#!/usr/bin/env bash
# The game install sits next to the project folder, not inside it.
set -eu
mkdir -p ../elderwyn-install
cp -R "$(dirname "$0")/files/elderwyn-install/." ../elderwyn-install/

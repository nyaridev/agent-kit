#!/usr/bin/env bash
# The fixture's .gitignore is stored as "gitignore" so it doesn't hide the fixture's own _sdk/ files in this repo.
set -eu
cp -R "$(dirname "$0")/files/project/." .
mv gitignore .gitignore

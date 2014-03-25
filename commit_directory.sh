#!/bin/bash
# Stages all added files and changes to git and commits them.
#
# Usage: ./commit_directory directory_to_commit
# Usage: ./commit_directory /storage/docs-backup

cd $1

changed=$(git ls-files -m | tr '\n' ' ')
other=$(git ls-files -o | tr '\n' ' ')
date=$(date)

git add -A
git commit -am "Added: $other-- Changed: $changed on $date"

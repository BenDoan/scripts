#!/bin/bash
# Stages all added files and changes to git and commits them.
#
# Usage: ./commit_directory directory_to_commit
# Usage: ./commit_directory /storage/docs-backup

cd $1

# xargs trims a trailing space, only works for single lines
changed=$(git ls-files -m | tr '\n' ' ' | xargs echo)
other=$(git ls-files -o | tr '\n' ' ' | xargs echo)

message=""
if [ "" != "$other" ]; then
    message="$message""Added $other"
fi
if [ "" != "$other" ] && [ "" != "$changed" ]; then
    message="$message""  --  "
fi
if [ "" != "$changed" ]; then
    message="$message""Changed $changed"
fi
message="$message"" on $(date)"

git add -A . > /dev/null
git commit -am "$message" > /dev/null

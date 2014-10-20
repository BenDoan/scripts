#!/bin/bash # Stages all added files and changes to git and commits them.
#
# Usage: ./commit_directory directory_to_commit
# Usage: ./commit_directory /storage/docs-backup

cd $1

changed=""
for c in $(git ls-files -m); do
    name=$(basename $c)
    changed="$changed""$name "
done

other=""
for c in $(git ls-files -o); do
    name=$(basename $c)
    other="$other""$name "
done

message=""
if [ "" != "$other" ]; then
    message="$message""Added $other"
fi
if [ "" != "$other" ] && [ "" != "$changed" ]; then
    message="$message"" --  "
fi
if [ "" != "$changed" ]; then
    message="$message""Changed $changed"
fi
message="$message"" on $(date)"

git add -A . > /dev/null
git commit -am "$message" > /dev/null

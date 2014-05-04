#!/bin/bash
# Performs an incremental backup to a remote client, and commits
# the changes to a git repository.  Depends on commit_directory.sh.
#
# Usage ./backup_to_remote directory_to_backup hostname host_location
# Usage ./backup_to_remote ~/documents ben-vps /storage/documents-backup

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

rsync -az $1 "$2:$3"
sync
cat $DIR/commit_directory.sh | ssh $2 "cat > /tmp/backup.sh ; chmod 755 /tmp/backup.sh ; /tmp/backup.sh $3 ; rm /tmp/backup.sh"

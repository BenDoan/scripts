#!/bin/bash
# Performs an incremental backup to a remote client, and commits
# the changes to a git repository.  Depends on commit_directory.sh.
#
# Usage ./backup_to_remote directory_to_backup hostname host_location
# Usage ./backup_to_remote ~/documents ben-vps /storage/documents-backup

import perform
import sys
import os


from_dir = sys.argv[1]
hostname = sys.argv[2]
to_dir = sys.argv[3]
path = os.path.dirname(os.path.realpath(__file__))
run_script = "cat > /tmp/backup.sh ; chmod 755 /tmp/backup.sh ; /tmp/backup.sh %(to_dir) ; rm /tmp/backup.sh"

dir = ""

perform.rsync("-az", from_dir, "{}:{}".format(hostname, to_dir))
perform.sync()
perform._("cat %(path)/commit_directory.py | ssh %(hostname) %(run_script)

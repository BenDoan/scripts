#!/usr/bin/python

# Stages all added files and changes to git and commits them.
#
# Usage: ./commit_directory directory_to_commit
# Usage: ./commit_directory /storage/docs-backup

import sys, os
import perform

if len(sys.argv) > 0:
    os.chdir(sys.argv[1])

changed = " ".join(map(perform.basename, perform.git("ls-files", "-m").split("\n")))
other = " ".join(map(perform.basename, perform.git("ls-files", "-o").split("\n")))
message = "Added {} -- Changed {}".format(changed, other)

perform.git("add", "-A", ".")
perform.git("commit", "-am", message)

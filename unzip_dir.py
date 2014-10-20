#!/usr/bin/python

# unzips all .zip files in the cwd into folders with the names of the zip files
# The directory defaults to the cwd
# Usage: ./unzip_dir.py [directory]

import os, sys, glob
import perform

if len(sys.argv) > 0:
    os.chdir(sys.argv[1])

for f in glob.glob("*.zip"):
    dir_name = perform.basename(f, ".zip")
    perform.mkdir(dir_name)
    perform.unzip(f, "-d", dir_name)

#!/bin/bash
# does a fresh backup of the home drive

dir=`date +%d-%b-%y`
mkdir $dir
rsync -avh /home/ben /media/Backup/desktop/full/$dir
